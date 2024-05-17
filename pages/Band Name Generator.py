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
    bandName = set()
    for i in range(7):
        bandName.add(prompt[randrange(len(prompt))] + " " + prompt[randrange(len(prompt))])
        
    for i in bandName:
        st.info(i)