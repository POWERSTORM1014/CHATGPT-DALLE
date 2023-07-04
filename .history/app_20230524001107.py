import streamlit as st
import openai
import time

delay_time = 0.01  #  faster
max_response_length = 200
answer = ""
start_time = time.time()

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
            model="gpt-3.5-turbo",
            messages=gpt_prompt,
            max_tokens=max_response_length,
            temperature=0,
            stream=True,
        )
        prompt = gpt_response["choices"][0]["message"]["content"]
        st.write(prompt)
