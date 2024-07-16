import streamlit as st
from random import randrange

st.title("BandName Generator")

prompt = [
st.text_input("Enter the name of your native place: "),
st.text_input("Enter the name of your Genre"),
st.text_input("Enter the name of your pet"),
st.text_input("Enter the name of a sport you can relate to"),
st.text_input("Enter the name of Random Word")
]

with st.expander("Possible Band names"):
    for i in range(5):
        st.info(prompt[randrange(len(prompt))] + " " + prompt[randrange(len(prompt))])