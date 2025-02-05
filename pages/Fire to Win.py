import streamlit as st
from random import randrange
import pandas as pd
st.title("Destroy the Tower!!!")
with st.expander("Rules"):
    st.table([
        "Welcome to Destroy the Tower Game!!!",
        "Fire 10 units on opponents tower to win!",
        "If your tower gets more than 5 hits, you loose.",
        "You can fire from the towers getting damage, to reduce the damage."
    ])

if 'mat' not in st.session_state:
    st.session_state['mat'] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]
# st.table(st.session_state['mat'])
st.bar_chart(st.session_state['mat'][1])
def option1():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][0] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]

def option2():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][1] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]
    
def option3():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][2] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]

col0, col1, col2, col3 = st.columns(4)
col1.button("Canon 1", on_click=option1)
col2.button('Canon 2', on_click=option2)
col3.button('Canon 3', on_click=option3)


@st.experimental_dialog("You Win!!!")
def Win():
    st.table(pd.DataFrame(
        data=[st.session_state['mat'][1]],
        columns=['Tower 1', 'Tower 2', 'Tower 3']
    ))
    st.link_button("Explore more!!", "https://victoriousmango.github.io/Portfolio/")

@st.experimental_dialog("You Lost!!!")
def Lost():
    st.table(pd.DataFrame(
        data=[st.session_state['mat'][1]],
        columns=['Tower 1', 'Tower 2', 'Tower 3']
    ))
    st.link_button("Explore more!!", "https://victoriousmango.github.io/Portfolio/")

for i in st.session_state['mat'][1]:
    if i > 9:
        Win()
    if i < -5:
        Lost()