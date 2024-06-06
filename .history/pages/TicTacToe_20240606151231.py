import streamlit as st

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

    def shoot():
        
        return "Comparing!!!"
    
Game = RPS
st.write(Game.isRock())
st.write(Game.isScissor())
st.write(Game.isPaper())