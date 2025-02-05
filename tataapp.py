import yfinance as yf
import pandas as pd

import streamlit as st
st.title('TataPower')

ticker=st.sidebar.text_input("Enter Stock Ticker","TATAPOWER.NS")
start_date=st.sidebar.text_input("Start Date","2020-01-01")
end_date=st.sidebar.text_input("End date","2025-02-01")

@st.cache_data
def load_data(ticker,start_date,end_date):
    data=yf.download(ticker,start=start_date,end=end_date)
    return data

data=load_data(ticker,start_date,end_date)


st.subheader('Raw data')
st.write(data)
