import streamlit as st
import smtplib
import pandas as pd

class Distributor():
    def __init__(self, numberOfPeople, TotalAmount):
        self.numberOfPeople = numberOfPeople
        self.TotalAmount = TotalAmount
        self.Log = pd.DataFrame(columns=['Who Paid', 'Item', 'How much Paid', 'Contributors'])
        self.BalanceTable = pd.DataFrame(columns=['Name', 'Have Spent', 'Will Receive', 'Net Total'])
    
    def log(self, entryNumber):
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1]) 
        self.Log.loc[len(self.Log.index)] = [
            col1.text_input(f"Who has Paid - Transaction:{entryNumber}"), 
            col2.text_input(f"Item Paid For - Transaction:{entryNumber}"),
            col3.number_input(f"How Much Paid - Transaction:{entryNumber}"), 
            [i.strip() for i in col4.text_input(f"Contributors - Transaction:{entryNumber}").split(',')]
            ]
        if col5.select_slider(f"Log Transaction:{entryNumber+1}", options=['No', 'Yes']) == 'Yes':
            entryNumber+=1
            self.log(entryNumber)
    def EqualDistributor(self):
        return self.TotalAmount/self.numberOfPeople
    
    def BalanceSheet(self):
        Names = set(i for i in self.Log)

    def NonLinerDistribution(self):
        self.log(1)
        return self.Log


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
        
    