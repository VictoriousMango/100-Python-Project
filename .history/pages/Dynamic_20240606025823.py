import streamlit as st
mat = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
]

def option1(mat):
    mat[0][0] += 1
    st.table(mat)

def option2(mat):
    mat[0][1] += 1
    st.table(mat)

button = st.button("Option 1", on_click=option1)
button = st.button('Option 2', on_click=option2)
