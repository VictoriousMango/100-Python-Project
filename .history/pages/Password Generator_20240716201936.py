import streamlit as st
import random

smallAlphabet = [chr(i) for i in range(97, 123)]
CapitalAlphabet = [chr(i) for i in range(65, 91)]
specialCharacters = [chr(i) for i in range(33, 48)] + \
                          [chr(i) for i in range(58, 65)] + \
                          [chr(i) for i in range(91, 97)] + \
                          [chr(i) for i in range(123, 127)]
pwdLength = st.number_input("Enter the Length of the password") // 1
Strings = st.text_input("Enter string to include(separate with commas if multiple strings)").split(",")
Strings = [i.strip() for i in Strings]

setToUse = {
    1 : Strings,
    2 : smallAlphabet,
    3 : CapitalAlphabet,
    4 : specialCharacters
}

with st.expander("Suggested Passwords"):
    st.write(random.randint(1, len(setToUse.keys())))
    st.write(setToUse)