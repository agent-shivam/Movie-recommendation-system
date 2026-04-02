import streamlit as st
import requests

st.title("🎬 AI Movie Recommender")

query = st.text_input("Enter movie, genre, or mood")

if st.button("Recommend"):
    res = requests.get(f"http://127.0.0.1:8001/recommend?query={query}")
    data = res.json()

    for movie in data['recommendations']:
        st.write("🍿", movie)