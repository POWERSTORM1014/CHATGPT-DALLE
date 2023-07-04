import streamlit as st
import openai


st.title("내 생에 첫 인공지능앱")
openai.api_key = st.secrets["apikey"]
with st.form("form"):
    user_input = st.text_input("그림 주제를 입력하세요")
    submit = st.form_submit_button("그려줘!!!")

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
        with st.spinner("챗GPT 선생 생각중..."):
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=gpt_prompt
            )
        prompt = gpt_response["choices"][0]["message"]["content"]
        st.write(prompt)
