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

pd.set_option('display.max_columns', None)


def analyze_sentiment(df):
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('vader_lexicon')

    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    sia = SentimentIntensityAnalyzer()

    df['FEEDBACK'] = df['FEEDBACK'].str.lower()

    # removendo stopwords
    stop_words = set(stopwords.words('english'))
    df['FEEDBACK_NO_STOPWORDS'] = df['FEEDBACK'].apply(
        lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

    # aplicando o stemming
    df['FEEDBACK_STEMMING'] = df['FEEDBACK_NO_STOPWORDS'].apply(
        lambda x: ' '.join([stemmer.stem(word) for word in word_tokenize(x)]))

    # Aplica o lemmatizer
    df['FEEDBACK_LEMMATIZER'] = df['FEEDBACK_STEMMING'].apply(
        lambda x: ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(x)]))

    # Vectorizing the data
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['FEEDBACK_LEMMATIZER'])

    # Usando o SVM para classificar o sentimento
    svm = LinearSVC()
    svm.fit(X, df['SENTIMENT'])
    df['SENTIMENT_SVM'] = svm.predict(X)

    # Usando o Naive Bayes para classificar o sentimento
    nb = MultinomialNB()
    nb.fit(X, df['SENTIMENT'])
    df['SENTIMENT_NB'] = nb.predict(X)

    return df[['VEICULO', 'FEEDBACK', 'SENTIMENT_NLTK', 'COMPOUND']]
