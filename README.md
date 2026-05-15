#  SpamShield AI

SpamShield AI is a Machine Learning based Spam Detection System designed to classify both SMS messages and Emails as Spam or Not Spam using Natural Language Processing (NLP) techniques and Logistic Regression.

The project includes a modern interactive web application built using Streamlit where users can paste messages or emails and instantly receive predictions along with confidence scores.

---

#  Features

*  SMS Spam Detection
*  Email Spam Detection
*  NLP Text Preprocessing
*  TF-IDF Vectorization
*  Logistic Regression Models
*  Confidence Score Prediction
*  Modern Streamlit UI
*  Real-Time Detection System

---

#  Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* Streamlit
* Scikit-learn
* NLTK
* NumPy
* Pandas
* Pickle

---

#  Machine Learning Workflow

## 1. Data Collection

Two datasets were used in this project:

* `spam.csv` → SMS Spam Dataset
* `emails.csv` → Email Spam Dataset

---

## 2. Data Preprocessing

The text data was cleaned and transformed using:

* Lowercasing
* Tokenization
* Stopword Removal
* Punctuation Removal
* Stemming

---

## 3. Feature Extraction

TF-IDF (Term Frequency - Inverse Document Frequency) Vectorization was used to convert text into numerical feature vectors.

Configuration:

* Maximum Features: 10,000
* N-Gram Range: (1,2)

---

## 4. Model Training

The following machine learning models were tested:

* Naive Bayes
* Logistic Regression

After evaluation, Logistic Regression achieved the best performance for both SMS and Email spam detection.

---

#  Model Performance

## SMS Spam Detection

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.6% |
| Precision | 91%   |
| Recall    | 91%   |
| F1-Score  | 91%   |

---

## Email Spam Detection

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 99.4% |
| Precision | 98%   |
| Recall    | 99%   |
| F1-Score  | 99%   |

---

#  Evaluation Metrics Used

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

#  Saved Models

The trained models and vectorizers were saved using Pickle.

## Files

* `sms_model.pkl`
* `email_model.pkl`
* `sms_vectorizer.pkl`
* `email_vectorizer.pkl`

---

#  User Interface

The project includes:

* Dark-themed modern UI
* Interactive text input area
* Detection type selector
* Confidence score display
* Spam / Not Spam result cards

Built entirely using Streamlit.

---

#  Project Structure

```bash
SpamShield-AI/
│
├── app.py
├── spam.csv
├── emails.csv
├── sms_model.pkl
├── email_model.pkl
├── sms_vectorizer.pkl
├── email_vectorizer.pkl
├── requirements.txt
└── README.md
```

---

#  Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SpamShield-AI.git
```

## 2. Navigate to Project Folder

```bash
cd SpamShield-AI
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
streamlit run app.py
```

---

#  Future Improvements

* Deep Learning Based Spam Detection
* Transformer Models (BERT)
* Multi-language Spam Classification
* Cloud Deployment
* Spam Analytics Dashboard
* User Authentication System

---

#  Conclusion

SpamShield AI demonstrates the practical application of Machine Learning and Natural Language Processing techniques for solving real-world spam detection problems.

The project achieved high accuracy and strong performance using TF-IDF Vectorization with Logistic Regression, making it an effective solution for detecting both SMS and Email spam.

---

#  Author

Maureen Morris
