import streamlit as st
mat = list()
def define():
    mat = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
def option1():
    global mat
    mat[0][0] += 1
    st.table(mat)

def option2():
    global mat 
    mat[0][1] += 1
    st.table(mat)

button = st.button("Option 1", on_click=option1)
button = st.button('Option 2', on_click=option2)
button = st.button("Define", on_click=define)