import os
import pandas as pd
import numpy as np
import nltk
import re

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to dataset
DATA_PATH = os.path.join(BASE_DIR, "dataset", "spam.csv")


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

df = pd.read_csv(DATA_PATH, encoding="latin-1")


# Dataset already has correct columns
# text -> email content
# spam -> label (0 = legit, 1 = spam)

df = df[['text', 'spam']]
df.columns = ['text', 'label']
df['clean_text'] = df['text'].apply(clean_text)

tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['clean_text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

import pickle

pickle.dump(model, open("model/spam_model.pkl", "wb"))
pickle.dump(tfidf, open("model/tfidf.pkl", "wb"))

import pickle

with open("model/spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("Model and vectorizer saved successfully")
