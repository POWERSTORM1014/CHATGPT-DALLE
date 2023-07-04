import streamlit as st
import openai
import time

st.title("ChatGPT Plus DALL-E")
openai.api_key = st.secrets["apikey"]

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

    if submit and user_input:
        gpt_prompt = [
            {
                "role": "system",
                "content": "You are a docent in an art museum. Your role is to vividly describe the given image as if you're showing it to a museum visitor. Your description should be detailed and run approximately three sentences.",
            }
        ]

        gpt_prompt.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=gpt_prompt
        )

        responses = gpt_response["choices"][0]["message"]["content"].split(". ")
        temp_text = st.empty()

        for sentence in responses:
            sentence = sentence + "."
            temp_text.text(sentence)
            time.sleep(0.5)

        st.write(gpt_response["choices"][0]["message"]["content"])
