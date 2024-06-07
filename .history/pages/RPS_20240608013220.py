import streamlit as st
from random import randrange
import pandas as pd

col11=st.columns(1) #Title
col21=st.columns(1) #Rules
col31=st.columns(1) #Table1
col41=st.columns(1) #Table2
col51, col52, col52=st.columns(3) #User Choice
col11.title("Rock Paper Scissor")
with col21.expander("Rules"):
    st.table([
        "Welcome to Game of Rock Paper Scissors!!!.",
        'Test your luck.',
        'Whoever wins 10 rounds first, wins.',
        'Check your luck, with this game, after the results.'
    ])

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
    mat = [[st.session_state['PlayerScore'], st.session_state['ComputerScore'], st.session_state['#Draw']]]
    col31.table(pd.DataFrame(
        data = [[st.session_state['Player'], st.session_state['Computer']]],
        columns= ['Player', 'Computer']
        ))
    col41.table(pd.DataFrame(
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

# col1, col2, col3 = st.columns(3)
col51.button("🪨", on_click=isRock)
col52.button("📄", on_click=isPaper)
col53.button("✂️", on_click=isScissor)

@st.experimental_dialog("You Win!!!")
def Win():
    mat = [[st.session_state['PlayerScore'], st.session_state['ComputerScore'], st.session_state['#Draw']]]
    st.table(pd.DataFrame(
        data=mat, 
        columns=['Your Score', 'Computers Score', 'Number of Draws']
        ))
    st.link_button("Explore more!!", "https://victoriousmango.github.io/Portfolio/")

@st.experimental_dialog("You Lost!!!")
def Lost():
    mat = [[st.session_state['PlayerScore'], st.session_state['ComputerScore'], st.session_state['#Draw']]]
    st.table(pd.DataFrame(
        data=mat, 
        columns=['Your Score', 'Computers Score', 'Number of Draws']
        ))
    st.link_button("Explore more!!", "https://victoriousmango.github.io/Portfolio/")

if st.session_state['PlayerScore'] > 9:
    Win()
if st.session_state['ComputerScore'] > 9:
    Lost()