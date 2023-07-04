import streamlit as st
import openai

st.title("내 생에 첫 인공지능앱")
openai.api_key = st.secrets["apikey"]
with st.form("form"):
    user_input = st.text_input("그림 주제를 입력하세요(영어로)")
    image_size = st.selectbox("그림 크기를 선택하세요", ("1024x1024", "512x512", "256x256"))
    submit = st.form_submit_button("그려줘!!!")
    if submit and user_input:
        gpt_prompt = [
            {
                "role": "system",
                "content": "You are a webtoon artist specializing in drawing emoticons. Your task is to create a vivid written depiction of an emoticon based on provided adjectives or words. Your description should be detailed and condensed into approximately two sentences. Please respond in English.",
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
        with st.spinner("그림 그리는중..."):
            dalle_response = openai.Image.create(prompt=prompt, size=image_size)
            st.image(dalle_response["data"][0]["url"])
