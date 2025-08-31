from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

prompt_patron = (
    
    "Genera un patron como si fuerasun diseñador experto en tejido."
    "Crea un patrón de suéter infantil, talles 4, 6 y 8, con lana semigruesa y agujas Nº5."
    " Incluye: Materiales y cantidad de lana por talle  Puntos iniciales y distribución de delantero y espalda"
    "  Instrucciones de sisa y cuello  Pasos claros y ordenados, listos para tejer  Se preciso, conciso y organiza la respuesta con títulos y subtítulos."

)

response = client.chat.completions.create(
    model="gemini-1.5-flash",
    messages=[
        {"role": "system", "content": "Eres experta en patrones de tejido."},
        {"role": "user", "content": prompt_patron}
    ],
    temperature=0.2,
    max_tokens=1000
)

# Acceder al contenido correctamente
print(response.choices[0].message.content)
