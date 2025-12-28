# 🛡️ MailSentry AI

### Intelligent Email Spam & Phishing Detection System

MailSentry AI is an end-to-end **AI-powered email security system** that detects spam emails in real time using **Natural Language Processing (NLP)** and **Machine Learning**, and integrates directly into Gmail via a **Chrome Extension**.

The system analyzes email content, classifies it as **Spam or Legitimate**, and provides instant feedback inside the user's inbox.

---

## 📌 Why MailSentry AI?

Email spam and phishing attacks are increasing rapidly, causing:

* Data breaches
* Financial fraud
* Identity theft

MailSentry AI acts as a **personal email guard**, intelligently filtering suspicious emails before users interact with them.

---

## 🚀 Key Features

* ✅ Machine Learning–based spam classification
* ✅ NLP text preprocessing (tokenization, stemming, stopword removal)
* ✅ Real-time prediction via FastAPI
* ✅ Gmail Chrome Extension integration
* ✅ Lightweight & fast inference
* ✅ Modular and scalable architecture

---

## 🧠 How It Works (High-Level Flow)

```
Gmail Email Content
        ↓
Chrome Extension (Reads Email Text)
        ↓
FastAPI Backend (REST API)
        ↓
ML Model (TF-IDF + Naive Bayes)
        ↓
Spam / Not Spam Prediction
```

---

## 🏗️ Project Architecture

```
MailSentry-AI/
│
├── app/
│   └── api.py                # FastAPI backend
│
├── model/
│   ├── train_model.py        # Model training script
│   ├── spam_model.pkl        # Trained ML model
│   └── tfidf.pkl             # TF-IDF vectorizer
│
├── dataset/
│   └── spam.csv              # Email dataset
│
├── chrome-extension/
│   ├── manifest.json         # Chrome extension config
│   └── content.js            # Gmail DOM reader
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Machine Learning Details

### 🔹 Dataset

* Labeled email dataset (`spam.csv`)
* Classes:

  * `0` → Not Spam (Ham)
  * `1` → Spam

### 🔹 Text Preprocessing

* Lowercasing
* Removing special characters
* Tokenization
* Stopword removal (NLTK)
* Stemming (Porter Stemmer)

### 🔹 Feature Engineering

* **TF-IDF Vectorization**
* Max features: 5000

### 🔹 Model

* **Multinomial Naive Bayes**
* Lightweight, fast, and effective for text classification

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/MailSentry-AI.git
cd MailSentry-AI
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the Model (Optional)

```bash
python model/train_model.py
```

---

### 5️⃣ Run the Backend API

```bash
uvicorn app.api:app --reload
```

API will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 API Usage

### 🔹 Endpoint

```
POST /predict
```

### 🔹 Request Body

```json
{
  "email": "Congratulations! You have won a free prize."
}
```

### 🔹 Response

```json
{
  "prediction": "Spam"
}
```

---

## 🧩 Chrome Extension Setup

1. Open Chrome and go to:

   ```
   chrome://extensions
   ```
2. Enable **Developer Mode**
3. Click **Load Unpacked**
4. Select the `chrome-extension/` folder
5. Open Gmail and click on any email
6. Spam detection result appears instantly

---

## 🧑‍💻 Real-World Use Case

* Detects spam emails **inside Gmail**
* Can be extended to:

  * Outlook
  * Yahoo Mail
  * Corporate email systems
* Suitable for:

  * Individuals
  * Enterprises
  * Cybersecurity solutions

---

## 📈 Performance

* High accuracy on benchmark spam dataset
* Low latency inference
* Optimized for real-time detection

---

## 🔮 Future Enhancements

* 🚀 Phishing URL detection
* 🚀 Deep Learning (LSTM / BERT)
* 🚀 Cloud deployment (AWS / Azure)
* 🚀 Gmail UI warning banners
* 🚀 User feedback loop for retraining

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn**
* **NLTK**
* **Pandas**
* **FastAPI**
* **JavaScript**
* **Chrome Extensions API**

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

**Anshika**
Computer Science Engineer | Software Developer
Passionate about AI, NLP, and real-world system design

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub — it really helps!

