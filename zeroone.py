from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()  # Carga las variables desde tu archivo .env

# Inicializar cliente
client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Prompt One-shot
prompt_tabla = """
Ejemplo:  
Suéter talla XS, lana fina, punto vareta y elástico:  
- Largo total: 40 cm  
- Ancho pecho: 30 cm  
- Largo de manga: 15 cm  
- Sisa: 18 cm  
- Cuello: 10 cm  
- Observaciones: usar punto elástico en puños y borde inferior  

Ahora, como diseñador experto en crochet, genera una tabla de medidas para un suéter básico infantil en lana semigruesa, talles S, M y L, usando punto vareta y elástico. Incluye:  
- Largo total  
- Ancho de pecho  
- Largo de manga  
- Sisa  
- Cuello  
- Notas opcionales sobre el tejido
"""

# Generar la tabla de medidas
response = client.chat.completions.create(
    model="gemini-1.5-flash",
    messages=[{"role": "user", "content": prompt_tabla}],
    temperature=0.2,
    max_tokens=800
)

# Extraer contenido
print(response.choices[0].message.content)

archivo = "tabla_medidas_sueter.txt"
with open(archivo, "w", encoding="utf-8") as f:
    f.write(tabla_medidas)

print(f"\n✅ Tabla de medidas generada y guardada en '{archivo}'\n")

