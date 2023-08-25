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
            {"role": "system", "content": '''Você é uma inteligência artificial que analisa dados e previsões desses 
            dados, onde vamos te dar os dados em um formato de lista com eixo x e y, e você pode explicar o que são 
            esses dados e dar uma previsão do que pode nos entregar no futuro, qualquer assunto que não seja 
            relacionado a dados você responderá "Não Sei". O limite de resposta é de até 80 caracteres. Se você não 
            enxergar um padrão você pode dar uma hipotese, porém sempre deixe claro que é uma hipotese. Em todo começo 
            de uma resposta sempre fala "De acordo com gráfico..."'''},
            {"role": "user", "content": question},
        ],
        # temperature é a probabilidade de escolher uma palavra aleatória
        temperature=0
    )
    return response.choices[0]['message']['content']

