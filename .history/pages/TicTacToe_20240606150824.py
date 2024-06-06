import streamlit as st

class RPS():
    def __init__(self):
        pass

    def isRock():
        return "Rock"
    def isScissor():
        return "Scissor"
    def isPaper():
        return "Paper"

    def shoot():
        return "Comparing!!!"
    
Game = RPS()
st.write(Game.isRock())