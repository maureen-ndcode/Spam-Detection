import streamlit as st
import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="centered"
)
nltk.download('stopwords')
sms_model = pickle.load(open('sms_model.pkl', 'rb'))
email_model = pickle.load(open('email_model.pkl', 'rb'))

sms_vectorizer = pickle.load(open('sms_vectorizer.pkl', 'rb'))
email_vectorizer = pickle.load(open('email_vectorizer.pkl', 'rb'))
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def transform_text(text):

    # Lowercase
    text = text.lower()

    # Split into words
    words = text.split()

    # Remove special characters
    clean_words = []

    for word in words:
        if word.isalnum():
            clean_words.append(word)

    # Remove stopwords
    filtered_words = []

    for word in clean_words:
        if word not in stop_words and word not in string.punctuation:
            filtered_words.append(word)

    # Stemming
    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(ps.stem(word))

    return " ".join(stemmed_words)

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to bottom right, #0a0f1f, #111827);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 40px;
    font-size: 1rem;
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.06);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
}

/* Text Area */
textarea {
    background-color: #1f2937 !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid #374151 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: bold;
}

/* Spam Result */
.spam-card {
    background: rgba(255,0,0,0.12);
    border: 1px solid rgba(255,0,0,0.3);
    padding: 20px;
    border-radius: 18px;
    margin-top: 25px;
    text-align: center;
}

/* Ham Result */
.ham-card {
    background: rgba(0,255,100,0.12);
    border: 1px solid rgba(0,255,100,0.3);
    padding: 20px;
    border-radius: 18px;
    margin-top: 25px;
    text-align: center;
}

/* Result Text */
.result-text {
    font-size: 28px;
    font-weight: bold;
}

/* Confidence */
.confidence {
    margin-top: 10px;
    color: #d1d5db;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
🛡️ SpamShield AI
</div>

<div class="subtitle">
Intelligent SMS & Email Spam Detection System
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Select Detection Type
detection_type = st.selectbox(
    "Select Detection Type",
    ["SMS Detection", "Email Detection"]
)

# User Input
input_text = st.text_area(
    "Enter your message",
    height=200,
    placeholder="Paste your SMS or Email here..."
)

# Predict Button
predict_btn = st.button("🚀 Analyze Message")

st.markdown('</div>', unsafe_allow_html=True)

if predict_btn:

    # Empty Input Check
    if input_text.strip() == "":

        st.warning("Please enter a message.")

    else:

        # Preprocess Text
        transformed = transform_text(input_text)

        # ==============================
        # SMS DETECTION
        # ==============================

        if detection_type == "SMS Detection":

            vector_input = sms_vectorizer.transform([transformed])

            prediction = sms_model.predict(vector_input)[0]

            probability = sms_model.predict_proba(vector_input)[0]

        
        else:

            vector_input = email_vectorizer.transform([transformed])

            prediction = email_model.predict(vector_input)[0]

            probability = email_model.predict_proba(vector_input)[0]

        # Confidence Score
        confidence = round(max(probability) * 100, 2)
       

        if prediction == 1:

            st.markdown(f"""
            <div class="spam-card">

            <div class="result-text">
                🚨 SPAM DETECTED
            </div>

            <div class="confidence">
                Confidence Score: {confidence}%
            </div>

            </div>
             """, unsafe_allow_html=True)

        else:
            

            st.markdown(f"""
            <div class="ham-card">

            <div class="result-text">
                ✅ NOT SPAM
            </div>

            <div class="confidence">
                Confidence Score: {confidence}%
            </div>

            </div>
        """, unsafe_allow_html=True)