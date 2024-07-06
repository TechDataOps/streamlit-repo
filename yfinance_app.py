import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#tickerSymbol = 'GOOGL'

# Input field for user to enter ticker symbol
tickerSymbol = st.text_input("Enter Stock Ticker Symbol (e.g., GOOGL for Google) ")

if tickerSymbol:
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    st.write(f"Shown are the stock **closing price** and ***volume*** of {tickerSymbol}!")
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2024-01-01', end='2024-07-07')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)
    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)
else:
    st.write("Enter a ticker symbol")
  
