import streamlit as st
from random import randrange
import pandas as pd

### Enter Player Name
@st.experimental_dialog("User Info")
def Player():
    st.session_state['PlayerName'] = st.text_input("Because...")
    if st.button("Submit"):
        st.rerun()

st.title("Rock Paper Scissor")
with st.expander("Rules"):
    st.table([
        "Welcome to Game of Rock Paper Scissors!!!.",
        'Test your luck.',
        'Whoever wins 10 rounds first, wins.',
        'Check your luck, with this game, after the results.'
    ])

for i in ['Player', 'Computer', 'PlayerScore', 'ComputerScore', '#Draw', 'PlayerName']:
    if i not in st.session_state:
        st.session_state[i] = 0
if st.session_state['PlayerName'] == 0:
    Player()

def shoot():
    st.session_state['Computer'] = ['Rock', 'Paper', 'Scissor'][randrange(3)]
    winCriteria = [
        st.session_state['Player'] == 'Rock' and st.session_state['Computer'] == 'Scissor' or
        st.session_state['Player'] == 'Paper' and st.session_state['Computer'] == 'Rock' or
        st.session_state['Player'] == 'Scissor' and st.session_state['Computer'] == 'Paper'   
    ]
    if st.session_state['Player'] == st.session_state['Computer']:
        st.session_state['#Draw'] += 1
        # st.info(f"Draw : {st.session_state['Player']} # {st.session_state['Computer']}")
    elif winCriteria[0]:
        st.session_state['PlayerScore'] += 1
        # st.success(f"You Won the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
        st.balloons()
    else:
        st.session_state['ComputerScore'] += 1
        # st.error(f"You Lost the duel : {st.session_state['Player']} # {st.session_state['Computer']}")
        st.snow()



def isRock():
    st.session_state['Player'] = 'Rock'
    shoot()

def isPaper():
    st.session_state['Player'] = 'Paper'
    shoot()

def isScissor():
    st.session_state['Player'] = 'Scissor'
    shoot()

col1, col2, col3 = st.columns(3)
col1.button("🪨", on_click=isRock)
col2.button("📄", on_click=isPaper)
col3.button("✂️", on_click=isScissor)

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
converter={
    'Rock': '🪨',
    'Paper': '📄',
    'Scissor': '✂️'
}
st.table(pd.DataFrame(
    data=[[st.session_state['PlayerScore'], st.session_state['ComputerScore'], st.session_state['#Draw']]], 
    columns=['Your Score', 'Computers Score', 'Number of Draws']
    ))
if st.session_state['Player'] and st.session_state['Computer']:
    results = st.table(pd.DataFrame(
        data = [[converter[st.session_state['Player']], converter[st.session_state['Computer']]]],
        columns= [st.session_state['PlayerName'], 'Computer']
        ))
    