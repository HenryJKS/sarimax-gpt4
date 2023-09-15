# Fazer uma classificação de sentimento com base em um dataframe
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import re

pd.set_option('display.max_columns', None)

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


df = pd.read_csv('C:\\Users\\Henry Sato\\Desktop\\ProjectChallenge\\ChatBotWeb\\assets\\teste.csv', sep=',')

# Training model for sentiment analysis
# 1. Cleaning data
# 2. Tokenization
# 3. Stopwords
# 4. Stemming
# 5. Lemmatization
# 6. Vectorization
# 7. Training model
