# Fazer uma classificação de sentimento com base em um dataframe
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

pd.set_option('display.max_columns', None)


df = pd.read_csv('C:\\Users\\Henry Sato\\Desktop\\ProjectChallenge\\ChatBotWeb\\assets\\modelotreino.csv', sep=',')

X = df['FEEDBACK']
Y = df['SENTIMENTO']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Criado o vetorizador
vectorizer = CountVectorizer(stop_words=stopwords.words('english'), tokenizer=word_tokenize)
x_train_count = vectorizer.fit_transform(X_train)

# Treinando com random forest
clf = MultinomialNB()
clf.fit(x_train_count, y_train)

# Testando o classificador nos dados de teste
X_test_counts = vectorizer.transform(X_test)
y_pred = clf.predict(X_test_counts)

# Imprimindo a acurácia do classificador
print("Acurácia: ", accuracy_score(y_test, y_pred))
