# 📰 Fake News Detection System

## 📌 Project Overview
This project is a Machine Learning based Fake News Detection System that classifies news articles as Real or Fake using Natural Language Processing (NLP) techniques.

## 🚀 Technologies Used
- Python
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- SQLite

## 📊 Model Accuracy
The Logistic Regression model achieved an accuracy of approximately **98.5%**.

## 🧠 How It Works
1. User enters news text.
2. Text is preprocessed using NLP techniques.
3. TF-IDF converts text into numerical format.
4. Logistic Regression predicts whether news is Real or Fake.
5. Result and confidence score are displayed.
6. Prediction history is stored in SQLite database.

## 💻 How To Run Locally
```bash
streamlit run streamlit_app.py