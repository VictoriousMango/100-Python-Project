import streamlit as st
import smtplib

class Distributor():
    def __init__(self, numberOfPeople, TotalAmount):
        self.numberOfPeople = numberOfPeople
        self.TotalAmount = TotalAmount
    
    def EqualDistributor(self):
        return self.TotalAmount/self.numberOfPeople

    def NonLinerDistribution(self):
        col1, col2, col3 = st.columns([1, 1, 1]) 
        
        distribution = []
        TotalAmount = self.TotalAmount
        while TotalAmount > 0:
            entry = [col1.text_input("Who Paid"), col2.number_input("How Much Paid"), col3.text_input("Who all will contribute")]
            distribution.append(entry)
            TotalAmount -= entry[1]
        return distribution

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
            st.info(f'Starting TLS Connection: {server.starttls()}')
            st.info(f'Logging in: {server.login(self.sender, self.password)}')
            server.sendmail(self.sender, self.receiver, self.message)
            print(f"Email Sent to: {self.receiver}")
        
st.title("Party Contributor!!!")

distributor = [
    st.number_input("Enter the Total Amount:"),
    st.number_input("Number of people:")
]



if st.button("Calculate Equal Distribution"):
    with st.spinner("Generating per person Contribution!!!"):
        message = Distributor(numberOfPeople=distributor[1], TotalAmount=distributor[0]).EqualDistributor()
    st.success(message)

if st.button("Calculate UnEqual Distribution"):
    with st.spinner("Generating per person Contribution!!!"):
        message = Distributor(numberOfPeople=distributor[1], TotalAmount=distributor[0]).NonLinerDistribution()
    st.table(message)
        
    