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
    st.session_state['Computer'] = ['Rock', 'Paper', 'Scissor'][randrange(3)]
    winCriteria = [
        st.session_state['Player'] == 'Rock' and st.session_state['Player'] == 'Scissor' or
        st.session_state['Player'] == 'Paper' and st.session_state['Player'] == 'Rock' or
        st.session_state['Player'] == 'Scissor' and st.session_state['Player'] == 'Paper'   
    ]
    if winCriteria[0]:
        st.success(f"You Won the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
        st.balloons()
    else:
        st.error(f"You Lost the duel : {st.session_state['Player']} # {st.session_state['Computer']}")


st.button("Rock", on_click=isRock)
st.button("Paper", on_click=isPaper)
st.button("Scissor", on_click=isScissor)
st.button("Shoot", on_click=shoot)