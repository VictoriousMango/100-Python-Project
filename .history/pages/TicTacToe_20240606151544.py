import streamlit as st
from random import randrange

class RPS():
    def __init__(self):
        self.Player
        self.Computer
        pass

    def isRock(self):
        self.Player = "Rock"
        return "Rock"
    def isScissor(self):
        self.Player = "Scissor"
        return "Scissor"
    def isPaper(self):
        self.Player = "Paper"
        return "Paper"

    def shoot(self):
        self.Computer = ['Rock', 'Paper', 'Scissor'][randrange(3)]
        return f"{self.Player} : {self.Computer}"
    
Game = RPS
st.button("Rock", on_click=Game.isRock)
st.button("Paper", on_click=Game.isPaper)
st.button("Scissor", on_click=Game.isScissor)
st.button("Shoot", on_click=Game.shoot)