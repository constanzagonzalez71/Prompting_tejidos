from PIL import Image
import numpy as np
from fpdf import FPDF
from openai import OpenAI
import os
from dotenv import load_dotenv

# ---------------------------
# 🔹 Cargar variables de entorno
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# ---------------------------
# 🔹 Prompt para Gemini
prompt_gemini = (
    "Genera un patrón de chaleco de dama en español, con instrucciones claras "
    "para tejerlo con lana semigruesa y agujas Nº5, incluyendo materiales, "
    "medidas, montaje, y pasos detallados por pieza. Formato numerado y fácil de seguir."
)

# ---------------------------
# Llamada a Gemini
response = client.chat.completions.create(
    model="gemini-1.5-flash",
    messages=[
        {"role": "system", "content": "Eres experta en patrones de tejido."},
        {"role": "user", "content": prompt_gemini}
    ],
    temperature=0.2,
    max_tokens=1000
)

# ✅ Acceder correctamente al contenido
patron_gemini = response.choices[0].message.content

# Guardar patrón de Gemini en TXT
with open("patron_chaleco_gemini.txt", "w", encoding="utf-8") as f:
    f.write(patron_gemini)
print("✅ Patrón Gemini guardado en 'patron_chaleco_gemini.txt'")

# ---------------------------
# 🔹 Procesar imagen a patrón cuadriculado
archivo_imagen = "public/chalecodamero.jpeg"  # tu imagen
ancho_patron = 30
alto_patron = 30
colores_max = 6
tamano_cuadrito = 6  # mm en PDF

img = Image.open(archivo_imagen)
img = img.resize((ancho_patron, alto_patron), Image.NEAREST)
img = img.convert("P", palette=Image.ADAPTIVE, colors=colores_max)
array = np.array(img)

# Asignar símbolos a cada color
colores_unicos = np.unique(array)
simbolos = [chr(65+i) for i in range(len(colores_unicos))]
mapa_colores = {c: simbolos[i] for i, c in enumerate(colores_unicos)}

# Guardar colores RGB
palette = img.getpalette()
mapa_rgb = {}
for c in colores_unicos:
    idx = c*3
    mapa_rgb[c] = (palette[idx], palette[idx+1], palette[idx+2])

# Generar instrucciones fila por fila
instrucciones = []
for fila in array:
    fila_instr = []
    actual = fila[0]
    conteo = 1
    for c in fila[1:]:
        if c == actual:
            conteo += 1
        else:
            fila_instr.append(f"{conteo}{mapa_colores[actual]}")
            actual = c
            conteo = 1
    fila_instr.append(f"{conteo}{mapa_colores[actual]}")
    instrucciones.append(" ".join(fila_instr))

# ---------------------------
# 🔹 Crear PDF final
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Título
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Chaleco Dama - Patrón Completo", ln=True, align="C")
pdf.ln(5)

# Instrucciones de Gemini
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 6, "Instrucciones de Gemini:\n" + patron_gemini)
pdf.ln(5)

# Instrucciones de la imagen
pdf.set_font("Courier", "", 10)
pdf.multi_cell(0, 5, "Patrón generado a partir de la imagen (fila por fila):")
for i, fila in enumerate(instrucciones, start=1):
    pdf.cell(0, 4, f"Fila {i}: {fila}", ln=True)
pdf.ln(5)

# Dibujar cuadritos de colores
pdf.set_font("Arial", "", 8)
pdf.cell(0, 5, "Patrón gráfico de colores:")
pdf.ln(5)
x_inicial = pdf.get_x()
y_inicial = pdf.get_y()

for fila_idx, fila in enumerate(array):
    for col_idx, color in enumerate(fila):
        r, g, b = mapa_rgb[color]
        pdf.set_fill_color(r, g, b)
        pdf.rect(
            x_inicial + col_idx*tamano_cuadrito,
            y_inicial + fila_idx*tamano_cuadrito,
            tamano_cuadrito,
            tamano_cuadrito,
            style="F"
        )

pdf.ln(alto_patron * tamano_cuadrito + 5)

# Leyenda de colores
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 5, "Leyenda de colores:")
pdf.ln()
pdf.set_font("Arial", "", 10)
for c, s in mapa_colores.items():
    r, g, b = mapa_rgb[c]
    pdf.set_fill_color(r, g, b)
    pdf.rect(pdf.get_x(), pdf.get_y(), 6, 6, style="F")
    pdf.cell(10)
    pdf.cell(0, 5, f"{s} = Color {c}", ln=True)

# Guardar PDF
pdf.output("patron_chaleco_completo.pdf")
print("✅ PDF final generado: 'patron_chaleco_completo.pdf'")
