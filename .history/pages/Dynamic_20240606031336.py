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
    st.session_state['mat'][2][randrange(3)] += 1
    st.table(st.session_state['mat'])

def option2():
    st.session_state['mat'][2][1] += 1
    st.session_state['mat'][2][randrange(3)] += 1
    st.table(st.session_state['mat'])
    
def option3():
    st.session_state['mat'][2][2] += 1
    st.session_state['mat'][2][randrange(3)] += 1
    st.table(st.session_state['mat'])

st.button("Option 1", on_click=option1)
st.button('Option 2', on_click=option2)