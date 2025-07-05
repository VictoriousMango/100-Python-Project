import streamlit as st
import jwt
from datetime import datetime
import time
import plotly.express as px

# Session Management
if "gussed" not in st.session_state:
    st.session_state["gussed"] = False
if "timeUp" not in st.session_state:
    st.session_state["timeUp"] = False

st.title("Hangman Game")
play = st.toggle("Play Hangman")
# PlaceHolders in the site 
time_bar = st.empty()
col1, col2 = st.columns(2)
secret_message = col1.text_input("Enter a JWT encoded message")
numberOfWords = col2.text_input("Enter the the number of letters in each word, seperated by comma").split(",")
word_entry = st.empty()
NumberOfWord_barPlot = st.empty()

with word_entry.expander("Generate JWT"):
    jwt_message = st.text_input("Enter a message to encode:")
    jwt_secret = st.text_input("Enter a secret key:")
    if jwt_message and jwt_secret:
        try:
            st.success(f'Encoded JWT: {jwt.encode({"message": jwt_message}, jwt_secret, algorithm="HS256")}')
        except Exception as e:
            st.error(f"Error encoding JWT: {e}")
    else:
        st.warning("Please enter both message and secret key to generate JWT.")

if play:
    start_time = datetime.now().timestamp()
    formatted_time = datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
    end_time = 25 # 10 seconds later
    formatted_end_time = datetime.fromtimestamp(end_time+start_time).strftime("%H:%M:%S")



# Word to be guessed
try:
    numberOfWords=[int(w.strip()) for w in numberOfWords]
except:
    pass
x, y = [i for i in range(len(numberOfWords))], [w for w in numberOfWords]
px.bar(x=x, y=y, labels={'x': 'Words', 'y': 'Length of Words'}, title='Word Lengths').update_layout(showlegend=False)
# jwt_secret = jwt.encode({"message": "It is a very Grate Cars Movie"}, secret, algorithm="HS256")
# Actual Game Logic
if play:
    guessedWord = word_entry.text_input("Guess the word:", key="guess")
    NumberOfWord_barPlot.plotly_chart(px.bar(x=x, y=y, labels={'x': 'Words', 'y': 'Length of Words'}, title='Word Lengths'), use_container_width=True)
    try:
        jwt_decoded = jwt.decode(secret_message, guessedWord, algorithms=["HS256"])
        word_entry.success(f"Decoded Message: {jwt_decoded['message']}")
        st.balloons()
    except jwt.InvalidTokenError:
        while play:
            curr_time = datetime.now().strftime("%H:%M:%S")
            with time_bar.container():
                col1, col2, col3 = st.columns(3)
                col1.metric("Current Time", curr_time)
                col2.metric("Start Time", formatted_time)
                col3.metric("End Time", formatted_end_time)
                if datetime.now().timestamp() <= end_time + start_time:
                    st.progress((datetime.now().timestamp() - start_time)/end_time)
                else:
                    st.warning("Time's up!")
            # sec += 1
            time.sleep(1)
        st.error("Invalid guess! Try again.")
    