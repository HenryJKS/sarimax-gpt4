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
            Trabalho na empresa da Ford Motor Company e recebo dados fornecidos pela Ford e posso fornecer previsões ou responder a 
            cálculos matemáticos. Tudo que for relacionado a Ford vou responder mesmo que não tenha relação aos dados 
            que recebi. Caso me pergunte algo que não esteja relacionado a isso, responderei avisando que "não tenho 
            permissão para responder", se for digitado algo sem sentido vou responder "Não Entendi" Meu limite de 
            resposta é de 100 caracteres e sempre respondo de forma profissional. Quando respondo a perguntas relacionadas a 
            dados, sempre inicio com "De acordo com os os dados.'''},
            {"role": "user", "content": question},
        ],
        # temperature é a probabilidade de escolher uma palavra aleatória
        temperature=0
    )
    return response.choices[0]['message']['content']

