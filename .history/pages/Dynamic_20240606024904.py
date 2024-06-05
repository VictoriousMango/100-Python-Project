import streamlit as st
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
def option1():
    global a
    a += 1
    st.table([
        [a, b, c],
        [d, e, f]
    ])
def option2():
    global b 
    b += 1
    st.table([
        [a, b, c],
        [d, e, f]
    ])

button = st.button("Option 1", on_click=option1)
button = st.button('Option 2', on_click=option2)
