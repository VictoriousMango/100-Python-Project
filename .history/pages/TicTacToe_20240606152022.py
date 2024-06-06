import streamlit as st
from random import randrange

def isRock():
    global Player
    Player = "Rock"
    return "Rock"
def isScissor(self):
    global Player
    Player = "Scissor"
    return "Scissor"
def isPaper(self):
    global Player
    Player = "Paper"
    return "Paper"

def shoot(self):
    global Computer
    Computer = ['Rock', 'Paper', 'Scissor'][randrange(3)]
    return f"{self.Player} : {self.Computer}"
    
Game = RPS
rock=st.button("Rock")
if rock:
    Game.isRock()

st.button("Paper", on_click=Game.isPaper())
st.button("Scissor", on_click=Game.isScissor())
st.button("Shoot", on_click=Game.shoot())