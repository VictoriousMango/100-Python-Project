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

button1 = st.button("Option 1")
button2 = st.button('Option 2')

if button1:
    option1(mat)
if button2:
    option2(mat)