import streamlit as st
import openai
import os


st.title("welcome to my app")

openai.api_key = "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"
text=st.text_input("enter your qquestion")



openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
    engine="text-davinci-003",  # or another model
    prompt="Once upon a time, there was a wise old owl who",
    max_tokens=100
)

print(response.choices[0].text.strip())
