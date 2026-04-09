import streamlit as st
import joblib
import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("history.db", check_same_thread=False)
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    news TEXT,
    result TEXT,
    confidence REAL
)
""")
conn.commit()

# Load trained model
model = joblib.load("fake_news_model.pkl")

st.title("📰 Fake News Detection System")

st.write("Model Used: Logistic Regression")
st.write("Accuracy: 98.5%")

news_text = st.text_area("Enter News Text Here")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([news_text])
        probability = model.predict_proba([news_text])
        confidence = round(max(probability[0]) * 100, 2)

        if prediction[0] == 1:
            result_text = "Fake"
            st.error("🚨 This is FAKE News")
        else:
            result_text = "Real"
            st.success("✅ This is REAL News")

        st.write("Confidence:", confidence, "%")

        # Save to database
        c.execute("INSERT INTO predictions VALUES (?, ?, ?)",
                  (news_text, result_text, confidence))
        conn.commit()

st.markdown("---")
st.write("Developed using Machine Learning, TF-IDF Vectorization, and Logistic Regression.")

st.markdown("## 📜 Prediction History")

if st.button("Show Prediction History"):
    import pandas as pd

    c.execute("SELECT * FROM predictions")
    rows = c.fetchall()

    if len(rows) == 0:
        st.info("No prediction history found.")
    else:
        df = pd.DataFrame(rows, columns=["News", "Result", "Confidence (%)"])
        st.dataframe(df)


if st.button("Clear Prediction History"):
    c.execute("DELETE FROM predictions")
    conn.commit()
    st.success("History cleared successfully!")