import openai
from dotenv import load_dotenv
import os

load_dotenv()

API = os.getenv("API_OPENAI")

openai.api_key = API

# Prompt de teste
prompt = "em 2022 tivemos 100 vendas, e 2023 temos atualmente 50 vendas qual previsão de 2024? "

# Resposta da API
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
)

# Retornar a resposta
reply = response.choices[0].text.strip()

print(reply)