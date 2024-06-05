import streamlit as st
import smtplib
import pandas as pd

class Distributor():
    def __init__(self, numberOfPeople, TotalAmount):
        self.numberOfPeople = numberOfPeople
        self.TotalAmount = TotalAmount
        self.Log = pd.DataFrame(columns=['Who Paid', 'Item', 'How much Paid', 'Contributors'])
        self.BalanceTable = pd.DataFrame(columns=['Name', 'Have Spent', 'Will Receive', 'Net Total'])
        self.BalancePerPerson = {'Name':[], 'Have Spent':[], 'Will Receive':[], 'Net Total':[]}
    
    def entryBalancePerPerson(self, Name, Spent):
        self.BalancePerPerson['Name'].append(Name)
        self.BalancePerPerson['Have Spent'].append(Spent)
        self.BalancePerPerson['Will Receive'].append(0)
        self.BalancePerPerson['Net Total'].append(0)
    
    def EqualDistributor(self, TotalAmount, numberOfPeople):
        return TotalAmount/numberOfPeople
    
    def log(self, entryNumber):
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1]) 
        # Used for Logging
        self.Log.loc[len(self.Log.index)] = [
            col1.text_input(f"Who has Paid - Transaction:{entryNumber}"), 
            col2.text_input(f"Item Paid For - Transaction:{entryNumber}"),
            col3.number_input(f"How Much Paid - Transaction:{entryNumber}"), 
            [i.strip() for i in col4.text_input(f"Contributors - Transaction:{entryNumber}").split(',')]
            ]
        self.entryBalancePerPerson(self.Log.loc[len(self.Log.index) - 1][0], self.Log.loc[len(self.Log.index) - 1][2])
        for i in self.Log.loc[len(self.Log.index) - 1][3]:
            self.entryBalancePerPerson(i, self.EqualDistributor(self.Log.loc[len(self.Log.index) - 1][2], len(self.Log.loc[len(self.Log.index) - 1][3])))

        if col5.select_slider(f"Log Transaction:{entryNumber+1}", options=['No', 'Yes']) == 'Yes':
            entryNumber+=1
            self.log(entryNumber)
    
    
    def BalanceSheet(self):
        Names = list(set(list(i for i in self.Log["Who Paid"])))
        BalancePerPerson = {
            'Name': Names,
            'Have Spent': [0 for i in Names],
            'Will Receive': [0 for i in Names],
            'Net Total': [0 for i in Names]
        }

        return self.BalancePerPerson

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
        Party = Distributor(numberOfPeople=distributor[1], TotalAmount=distributor[0])
        Log = Party.NonLinerDistribution()
        BalanceSheet = Party.BalanceSheet()
st.table(Log)

with st.expander("Contribution per person Generated"):
    st.table(BalanceSheet)
    