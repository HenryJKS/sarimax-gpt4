import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("API")

openai.api_key = OPENAI_API_KEY

print(openai.Model.list())

prompt = "Olá"

response = openai.Completion.create(
    engine="davinci",  # Mecanismo usado
    prompt=prompt,
    max_tokens=10
)

answer = response.choices[0].text.strip()
print(answer)
