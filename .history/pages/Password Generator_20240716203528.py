import streamlit as st
import random

smallAlphabet = [chr(i) for i in range(97, 123)]
CapitalAlphabet = [chr(i) for i in range(65, 91)]
specialCharacters = [chr(i) for i in range(33, 48)] + \
                          [chr(i) for i in range(58, 65)] + \
                          [chr(i) for i in range(91, 97)] + \
                          [chr(i) for i in range(123, 127)]
pwdLength = int(st.number_input("Number characters in pwd") // 1)
st.info("Entered string will be treated as a single character for password generation")
Strings = st.text_input("Enter string to include(separate with commas if multiple strings)").split(",")
Strings = [i.strip() for i in Strings] + \
                          [" "]

setToUse = {
    1 : Strings,
    2 : smallAlphabet,
    3 : CapitalAlphabet,
    4 : specialCharacters
}

with st.expander("Suggested Passwords"):
    pwd = ["" for i in range(5)]
    for i in range(5):
        setInUse = 0
        for j in range(pwdLength):
            setInUse = random.randint(1, len(setToUse.keys()))                     ### To select a set randomly
            pwd[i] += setToUse[setInUse][random.randint(1, len(setToUse[setInUse]) - 1)] ### To select an Element randomly and show the password.
            ### Subtracting 1, as the len is last index + 1
    st.write(pwd)
    #st.write(setToUse)