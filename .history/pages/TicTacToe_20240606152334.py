import streamlit as st
from random import randrange

if 'Player' not in st.session_state:
    st.session_state['Player'] = 'Initialized'
if 'Computer' not in st.session_state:
    st.session_state['Computer'] = 'Initialized'

def isRock():
    st.session_state['Player'] = 'Rock'
def isPaper():
    st.session_state['Player'] = 'Paper'
def isScissor():
    st.session_state['Player'] = 'Scissor'
def shoot():
    pass

st.button("Rock", on_click=isPaper())
st.button("Paper", on_click=isPaper())
st.button("Scissor", on_click=isScissor())
st.button("Shoot", on_click=shoot())