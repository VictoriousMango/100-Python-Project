import streamlit as st
if 'mat' not in st.session_state:
    st.session_state['mat'] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]

def option1():
    st.session_state['mat'][0][0] += 1
    st.table()

def option2():
    st.session_state['mat'][0][1] += 1
    st.table()

button1 = st.button("Option 1", option1)
button2 = st.button('Option 2', option2)