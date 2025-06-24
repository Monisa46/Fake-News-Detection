import streamlit as st
import joblib

# Load from NEWS folder
model = joblib.load(r"C:\Users\HP440G4\Desktop\NEWS\fake_news_model.pkl")
tfidf = joblib.load(r"C:\Users\HP440G4\Desktop\NEWS\tfidf_vectorizer.pkl")

st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detector")
st.markdown("Enter a news article below to check if it's **Real or Fake**.")

user_input = st.text_area("🖊️ Enter News Article Text Here:", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_tfidf = tfidf.transform([user_input])
        prediction = model.predict(input_tfidf)[0]

        if prediction == 1:
            st.success("✅ This news is **Real**.")
        else:
            st.error("🚫 This news is **Fake**.")
