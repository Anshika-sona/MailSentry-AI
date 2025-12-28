import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

# Load model and vectorizer
model = pickle.load(open("model/spam_model.pkl", "rb"))
tfidf = pickle.load(open("model/tfidf.pkl", "rb"))

# Test email
email = input("Paste email content: ")

cleaned = clean_text(email)
vector = tfidf.transform([cleaned])
prediction = model.predict(vector)

if prediction[0] == 1:
    print("🚨 SPAM / FAKE EMAIL")
else:
    print("✅ LEGITIMATE EMAIL")
