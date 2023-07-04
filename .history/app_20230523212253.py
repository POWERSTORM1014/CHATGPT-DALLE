import streamlit as st

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit and user_input:
    st.write("You entered: ", user_input)
