import streamlit as st
import openai

st.title("나만의 이미지 생성기")
openai.api_key = st.secrets["apikey"]
with st.form("form"):
    user_input = st.text_input("간단한 이미지에 대한 설명을 적어주세요")
    image_size = st.selectbox("그림 크기를 선택하세요", ("1024x1024", "512x512", "256x256"))
    submit = st.form_submit_button("만들기")
    if submit and user_input:
        gpt_prompt = [
            {
                "role": "system",
                "content": "You are an art gallery docent with the unique ability to imagine and eloquently describe images based on simple words or phrases. Your goal is to portray these images in an artistic, picture-like style, creating a vivid mental image. Your descriptions should be concise, utilising rich vocabulary, and limited to approximately two sentences. Please respond in English.",
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
            dalle_response = openai.Image.create(prompt=prompt, size=image_size)
            st.image(dalle_response["data"][0]["url"])
