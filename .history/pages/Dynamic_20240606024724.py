import streamlit as st
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
def option1():
    a += 1
    st.table([
        [a, b, c],
        [d, e, f]
    ])
def option2():
    b += 1
    a, b, c, d, e, f = 1, 2, 3, 4, 5, 9
    st.table([
        [a, b, c],
        [d, e, f]
    ])

button = st.button("Option 1", on_click=option1)
button = st.button('Option 2', on_click=option2)
