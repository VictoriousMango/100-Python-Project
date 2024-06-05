import streamlit as st
def option1():
    a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
def option2():
    a, b, c, d, e, f = 1, 2, 3, 4, 5, 9

button = st.button("Option 1", on_click=option1)
button = st.button('Option 2', on_click=option2)
st.table([
    [a, b, c],
    [d, e, f]
])