import streamlit as st
import openai

st.title("이모티콘 제조기")
openai.api_key = st.secrets["apikey"]
with st.form("form"):
    user_input = st.text_input("어떤 이모티콘을 만들까요?")
    # image_size = st.selectbox("그림 크기를 선택하세요", ("1024x1024", "512x512", "256x256"))
    submit = st.form_submit_button("만들기")
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
        with st.spinner("그리는중..."):
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=gpt_prompt
            )
        prompt = gpt_response["choices"][0]["message"]["content"]
        st.write(prompt)
        with st.spinner("그림 그리는중..."):
            dalle_response = openai.Image.create(prompt=prompt, size="256x256")
            st.image(dalle_response["data"][0]["url"])
