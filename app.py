import streamlit as st
from utils import summarize, generate_image

st.title("Text to Summary to Image")
st.header("This is a simple web app that summarizes text and generate an image of the summary")

text = st.text_area("Enter your text below","Astronaut riding a bicyclr in the beach") #2-suppoer string

if st.button("Summarize and Generate Image"):
    if not text:
        st.error("Please Input a text in the text box")
    else:
        with st.spinner("summarizing..."):
            summary = summarize(text)
        with st.spinner("Generating Image..."):
            image = generate_image(summary)

        st.info(f"Summary: {summary}")
        st.image(image)



