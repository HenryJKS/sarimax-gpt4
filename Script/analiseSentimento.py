# Fazer uma classificação de sentimento com base em um dataframe
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
import re

pd.set_option('display.max_columns', None)

df = pd.read_csv('../ChatBotWeb/assets/modelotreino.csv', sep=',')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def clean_text(text):
    # Convertendo para minúsculas
    text = text.lower()
    # Removendo caracteres especiais
    text = re.sub(r'\W', ' ', text)
    # Removendo espaços extras
    text = re.sub(r'\s+', ' ', text)
    # Removendo números
    text = re.sub(r'\d+', '', text)
    # Tokenizando o texto
    words = text.split()
    # Removendo stopwords e lematizando as palavras
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)


df['FEEDBACK_LIMPO'] = df['FEEDBACK'].apply(clean_text)

# Codificar a coluna de sentimento para 0 e 1
le = LabelEncoder()
df['SENTIMENTO_COD'] = le.fit_transform(df['SENTIMENTO'])
# 0 - negativo, 1 - positivo

X = df['FEEDBACK_LIMPO']
Y = df['SENTIMENTO_COD']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Criando o vetorizador
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)

# Treinando o modelo Naive Bayes
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Testando o modelo nos dados de teste
X_test_counts = vectorizer.transform(X_test)
y_pred = clf.predict(X_test_counts)

# Imprimindo a acurácia do modelo
accuracy = round(accuracy_score(y_test, y_pred), 2)

# R2
r2 = round(clf.score(X_test_counts, y_test), 2)

# RMSE
rmse = round(np.sqrt(np.mean((y_test - y_pred) ** 2)), 2)

# MAE
mae = round(np.mean(np.abs(y_test - y_pred)), 2)




# Usando o modelo para classificar o sentimento de uma frase
def classificar_sentimento(df):

    df['FEEDBACK'] = df['FEEDBACK'].astype(str)
    df['FEEDBACK_LIMPO'] = df['FEEDBACK'].apply(clean_text)
    X = df['FEEDBACK_LIMPO']
    X_counts = vectorizer.transform(X)

    # Classificando o sentimento
    df['SENTIMENTO_PREDICT'] = clf.predict(X_counts)

    # Criando coluna com o sentimento
    df['SENTIMENTO_PREDICT'] = df['SENTIMENTO_PREDICT'].apply(lambda x: 'Positivo' if x == 1 else 'Negativo')

    return df[['VEICULO', 'FEEDBACK', 'SENTIMENTO_PREDICT']]

