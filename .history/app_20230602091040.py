import streamlit as st
import openai

st.title("뚱뚱한 고양이 이모티콘 제조기")
openai.api_key = st.secrets["apikey"]
with st.form("form"):
    user_input = st.text_input("만들고자 하는 행동이나 표정을 묘사해주세요.")
    # image_size = st.selectbox("그림 크기를 선택하세요", ("1024x1024", "512x512", "256x256"))
    submit = st.form_submit_button("만들기")
    if submit and user_input:
        gpt_prompt = [
            {
                "role": "system",
                "content": "You are a webtoon artist specializing in drawing only fat cat emoticons. Your task is to create a vivid written depiction of an emoticon based on provided adjectives or words. Your description should be detailed and condensed into approximately two sentences. Please respond in English.",
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
        with st.spinner("그림 그리는중..."):
            dalle_response = openai.Image.create(prompt=prompt, size="512x512")
            st.image(dalle_response["data"][0]["url"])
