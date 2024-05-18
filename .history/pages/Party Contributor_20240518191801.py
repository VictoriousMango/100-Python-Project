import streamlit as st
import smtplib

class Distributor():
    def __init__(self, numberOfPeople, TotalAmount):
        self.numberOfPeople = numberOfPeople
        self.TotalAmount = TotalAmount
        self.distribution = []
    
    def log(self, entryNumber):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1]) 
        self.distribution.append([
            col1.text_input(f"Who Paid - Transaction:{entryNumber}"), 
            col2.number_input(f"How Much Paid - Transaction:{entryNumber}"), 
            col3.text_input(f"Who all will contribute - Transaction:{entryNumber}")
            ])
            
        if col4.slider(f"Log Transaction:{entryNumber+1}", min_value=0, max_value=1) == 1:
            entryNumber+=1
            self.log(entryNumber)
    def EqualDistributor(self):
        return self.TotalAmount/self.numberOfPeople

    def NonLinerDistribution(self):
        TotalAmount = self.TotalAmount
        entry = self.log(1)
        return self.distribution


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

with st.expander("Log Distribution"):
    with st.spinner("Generating per person Contribution!!!"):
        message = Distributor(numberOfPeople=distributor[1], TotalAmount=distributor[0]).NonLinerDistribution()
    st.table(message)
        
    