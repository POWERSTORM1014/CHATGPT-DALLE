import streamlit as st
import openai

# use the API key in .streamlit/secrets.toml
st.secrets.load_config("secrets.toml")
openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [
        {
            "role": "system",
            "content": "Imagine the detail appearance of the following input. response it with a sentence.",
        }
    ]

    gpt_prompt.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    gpt_response = openai.Completion.create(model="gpt-3.5-turbo", messages=gpt_prompt)

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
