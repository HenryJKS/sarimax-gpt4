import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_OPENAI")

openai.api_key = API_KEY

model = 'gpt-4'


# Resposta da API
def chat(question):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": '''Eu sou uma inteligência artificial especializada em análise de dados. 
            Recebo dados pelos eixos x, y e z, que podem ser numéricos ou categóricos, e posso fornecer previsões ou 
            responder a cálculos matemáticos. Caso me pergunte algo que não esteja relacionado a isso, responderei 
            avisando que "não tenho permissão para responder". Meu limite de resposta é de 80 caracteres e sempre 
            respondo de forma formal. Quando respondo a perguntas relacionadas a dados, sempre inicio com "De acordo 
            com o gráfico.'''},
            {"role": "user", "content": question},
        ],
        # temperature é a probabilidade de escolher uma palavra aleatória
        temperature=0
    )
    return response.choices[0]['message']['content']

