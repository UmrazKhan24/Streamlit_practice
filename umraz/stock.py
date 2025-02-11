import yfinance as yf
import streamlit as st
msft = yf.Ticker("MSFT")
hist = msft.history(period="1d", start="2019-01-01", end="2023-01-01")
st.write(hist)


import datetime

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date", datetime.date(2019, 1, 1))


with col2:
    end_date = st.date_input("End date", datetime.date(2023, 1, 1))

ticker_symbol = st.text_input("Enter a ticker symbol", "AAPL", key="placeholder")
ticker_data = yf.Ticker(ticker_symbol)
ticker_hist = ticker_data.history(period="1d", start=start_date, end=end_date)
st.dataframe(ticker_hist)

st.write(
    """
    ## Daily closing price chart  """
)

st.line_chart(ticker_hist["Close"])
