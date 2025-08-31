from openai import OpenAI
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# ---------------------------
# 🔹 Configuración OpenAI / Gemini
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# ---------------------------
# 🔹 Prompt para Gemini
prompt_gemini = """
Genera un patrón de suéter infantil en español para talles 4 y 6,
a partir del patrón de ejemplo: Talle 2, 44 puntos, delantero 22, espalda 22, sisa 16 cm, cuello 4 cm.
Incluir materiales, cantidad de lana, tensión, instrucciones paso a paso, montaje,
y notas para ajustar talles. Formato claro y numerado.
"""

response = client.chat.completions.create(
    model="gemini-1.5-flash",
    messages=[
        {"role": "system", "content": "Eres experta en patrones de tejido."},
        {"role": "user", "content": prompt_gemini}
    ],
    temperature=0.2,
    max_tokens=1000
)

# ✅ Obtener contenido de Gemini
patron_gemini = response.choices[0].message.content

# Guardar patrón de Gemini en TXT
with open("patron_sueter_gemini.txt", "w", encoding="utf-8") as f:
    f.write(patron_gemini)
print("✅ Patrón Gemini guardado en 'patron_sueter_gemini.txt'")

# ---------------------------
# 🔹 Generar ilustración del suéter (talle 6)
ancho_delantero = 28
alto_delantero = 30
ancho_espalda = 28
alto_espalda = 30

color1 = "#FFD580"  # mostaza
color2 = "#B0E0E6"  # celeste pastel

# Patrón de puntos simple para ilustración
delantero = np.zeros((alto_delantero, ancho_delantero))
delantero[:, ::2] = 1  # alternancia horizontal (simula Santa Clara)

espalda = np.zeros((alto_espalda, ancho_espalda))
espalda[::2, :] = 1  # alternancia vertical (simula Jersey)

def dibujar_patron(ax, matriz, titulo):
    cmap = [color2, color1]
    ax.imshow(matriz, cmap=plt.cm.get_cmap('Pastel1', 2))
    ax.set_title(titulo)
    ax.axis("off")

fig, axs = plt.subplots(1, 2, figsize=(8, 6))
dibujar_patron(axs[0], delantero, "Frontal")
dibujar_patron(axs[1], espalda, "Trasera")
plt.tight_layout()
plt.show()

# ---------------------------
# 🔹 Crear PDF con patrón y esquema
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Suéter Infantil - Patrón y Esquema", ln=True, align="C")
pdf.ln(5)

# Instrucciones Gemini
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 6, "Instrucciones de Gemini:\n" + patron_gemini)
pdf.ln(5)

# Nota: para incluir la ilustración matplotlib en PDF
# Guardamos la figura como imagen temporal
fig.savefig("public/ilustracion2.png", dpi=150)
pdf.image("public/ilustracion2.png", x=10, y=pdf.get_y(), w=180)

pdf.output("patron_sueter_completo.pdf")
print("✅ PDF final generado: 'patron_sueter_completo.pdf'")
