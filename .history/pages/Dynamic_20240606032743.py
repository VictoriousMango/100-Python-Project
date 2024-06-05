import streamlit as st
from random import randrange

if 'mat' not in st.session_state:
    st.session_state['mat'] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]

def option1():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][0] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]
    st.table(st.session_state['mat'])

def option2():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][1] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]
    st.table(st.session_state['mat'])
    
def option3():
    st.session_state['mat'][0][randrange(3)] += 1
    st.session_state['mat'][2][2] += 1
    for i in range(3):
        st.session_state['mat'][1][i] = st.session_state['mat'][2][i] - st.session_state['mat'][0][i]
    st.table(st.session_state['mat'])

col0, col1, col2, col3 = st.columns(4)
col1.button("Option 1", on_click=option1)
col2.button('Option 2', on_click=option2)
col3.button('Option 3', on_click=option3)

st.bar_chart(st.session_state['mat'][1])