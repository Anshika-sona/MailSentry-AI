from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = FastAPI()

# Load model
model = pickle.load(open("model/spam_model.pkl", "rb"))
tfidf = pickle.load(open("model/tfidf.pkl", "rb"))

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

class EmailRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_email(email: EmailRequest):
    cleaned = clean_text(email.text)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)[0]

    return {
        "spam": bool(prediction)
    }
