from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

prompt_patron = (
    "Genera un patrón de suéter infantil, talles 4, 6 y 8, "
    "lana semigruesa, agujas Nº5. Explica paso a paso."
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
