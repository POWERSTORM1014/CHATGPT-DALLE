import streamlit as st

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
