import streamlit as st

smallAlphabet = [chr(i) for i in range(97, 123)]
CapitalAlphabet = [chr(i) for i in range(65, 91)]
specialCharacters = [chr(i) for i in range(33, 48)] + \
                          [chr(i) for i in range(58, 65)] + \
                          [chr(i) for i in range(91, 97)] + \
                          [chr(i) for i in range(123, 127)]
print(smallAlphabet)
print(CapitalAlphabet)
print(specialCharacters)