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
        server = smtplib.SMTP("smtp.gmail.com", 587)
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

email = Email(Requirements, message)

with st.spinner("Sending Email!!"):
    email.SendEmail()
    
st.success("Email Sent!")


        
    