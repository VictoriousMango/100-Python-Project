import streamlit as st
import smtplib

class Email ():
    # Constructor Class to construct all the required variables.
    def init(self, Requirements, message):
        self.sender = Requirements[0]
        self.password = Requirements[1]
        self.receiver = Requirements[2]
        self.message = message
        
    def SendEmail(self):
        with st.sidebar:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            st.info(f'Echoing server: {server.ehlo()}')
            server.starttls()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, self.message)
            print(f"Email Sent to: {self.receiver}")
        
st.title("Party Contributor!!!")

Requirements = [
    st.text_input("Enter your mail address"),
    st.text_input("Enter your password", type="password"),
    st.text_input(f"Enter the receiver's address  mail address")
]

message = "Testing"

st.write(Requirements)
st.write(message)

if st.button("Send Email!!!"):
    with st.spinner("Sending Email!!"):
        email = Email()
        email.sender = Requirements[0]
        email.password = Requirements[1]
        email.receiver = Requirements[2]
        email.message = message
        email.SendEmail()
    
    st.success("Email Sent!")


        
    