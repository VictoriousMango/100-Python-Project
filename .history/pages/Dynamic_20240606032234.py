import streamlit as st
from random import randrange

if 'mat' not in st.session_state:
    st.session_state['mat'] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]

def option1():
    st.session_state['mat'][2][0] += 1
    comp = randrange(3)
    st.session_state['mat'][0][comp] += 1
    st.session_state['mat'] = st.session_state['mat'][2][0] - st.session_state['mat'][0][comp]
    st.table(st.session_state['mat'])

def option2():
    st.session_state['mat'][2][1] += 1
    comp = randrange(3)
    st.session_state['mat'][0][comp] += 1
    st.session_state['mat'] = st.session_state['mat'][2][1] - st.session_state['mat'][0][comp]
    st.table(st.session_state['mat'])
    
def option3():
    st.session_state['mat'][2][2] += 1
    comp = randrange(3)
    st.session_state['mat'][0][comp] += 1
    st.session_state['mat'] = st.session_state['mat'][2][2] - st.session_state['mat'][0][comp]
    st.table(st.session_state['mat'])

col0, col1, col2, col3 = st.columns(4)
col1.button("Option 1", on_click=option1)
col2.button('Option 2', on_click=option2)
col3.button('Option 3', on_click=option3)