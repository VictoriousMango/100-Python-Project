import streamlit as st
from random import randrange
import pandas as pd

for i in ['Player', 'Computer', 'PlayerScore', 'ComputerScore', '#Draw']:
    if i not in st.session_state:
        st.session_state[i] = None

def shoot():
    st.session_state['Computer'] = ['Rock', 'Paper', 'Scissor'][randrange(3)]
    winCriteria = [
        st.session_state['Player'] == 'Rock' and st.session_state['Computer'] == 'Scissor' or
        st.session_state['Player'] == 'Paper' and st.session_state['Computer'] == 'Rock' or
        st.session_state['Player'] == 'Scissor' and st.session_state['Computer'] == 'Paper'   
    ]
    if st.session_state['Player'] == st.session_state['Computer']:
        st.info(f"Draw : {st.session_state['Player']} # {st.session_state['Computer']}")
    elif winCriteria[0]:
        st.success(f"You Won the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
        st.balloons()
        
    else:
        st.error(f"You Lost the duel : {st.session_state['Player']} # {st.session_state['Computer']}")


def isRock():
    st.session_state['Player'] = 'Rock'
    shoot()

def isPaper():
    st.session_state['Player'] = 'Paper'
    shoot()

def isScissor():
    st.session_state['Player'] = 'Scissor'
    shoot()

st.button("Rock", on_click=isRock)
st.button("Paper", on_click=isPaper)
st.button("Scissor", on_click=isScissor)