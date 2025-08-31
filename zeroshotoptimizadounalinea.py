from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

prompt_patron = (
    "Patrón suéter infantil talles 4/6/8 en español — lana semigruesa, agujas Nº5 — entregar materiales (g/ovillos), tensión (p×h=10×10 cm), medidas cm, abreviaturas, instrucciones paso a paso por pieza con conteos por talle, montaje, lana por talle y nota para ajustar talles; formato claro y numerado."

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
