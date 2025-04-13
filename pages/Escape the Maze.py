import streamlit as st
import turtle
st.set_page_config(initial_sidebar_state="collapsed")

def T_Graphics():
    turtle.bgcolor("black")
    T = turtle.Turtle()
    T.pencolor("red")
    T.speed(1)
    T.forward(100)
    turtle.done()

st.button("Forward", on_click=T_Graphics)