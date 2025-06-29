

import streamlit as st
import pickle
from feature import FeatureExtraction



model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Phishing URL Detector")
st.title("🔍 Phishing URL Detection App")

url = st.text_input("Enter a URL to check if it's phishing or legitimate:")

if st.button("Check URL"):
    if url:
        with st.spinner("Extracting features and predicting..."):
            extractor = FeatureExtraction(url)
            features = extractor.extract_features()
            prediction = model.predict([features])[0]
            st.success("This is a legitimate website." if prediction == 1 else "⚠️ This is a phishing website!")
    else:
        st.warning("Please enter a valid URL.")
