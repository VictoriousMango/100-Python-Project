import streamlit as st
from random import randrange
import pandas as pd

for i in ['Player', 'Computer', 'PlayerScore', 'ComputerScore', '#Draw']:
    if i not in st.session_state:
        st.session_state[i] = 0

def shoot():
    st.session_state['Computer'] = ['Rock', 'Paper', 'Scissor'][randrange(3)]
    winCriteria = [
        st.session_state['Player'] == 'Rock' and st.session_state['Computer'] == 'Scissor' or
        st.session_state['Player'] == 'Paper' and st.session_state['Computer'] == 'Rock' or
        st.session_state['Player'] == 'Scissor' and st.session_state['Computer'] == 'Paper'   
    ]
    if st.session_state['Player'] == st.session_state['Computer']:
        st.session_state['#Draw'] += 1
        st.info(f"Draw : {st.session_state['Player']} # {st.session_state['Computer']}")
    elif winCriteria[0]:
        st.session_state['PlayerScore'] += 1
        st.success(f"You Won the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
        st.balloons()
    else:
        st.session_state['ComputerScore'] += 1
        st.error(f"You Lost the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
    mat = [st.session_state['PlayerScore'], st.session_state['ComputerScore'], st.session_state['#Draw']]
    st.write(mat)
    st.table(pd.DataFrame(
        data=mat, 
        columns=['Your Score', 'Computers Score', 'Number of Draws']
        ))


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