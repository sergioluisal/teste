import streamlit as st
import yfinance as yf

st.title("Teste yfinance")

try:
    ticker = yf.Ticker("AAPL")
    hist = ticker.history(period="5d")
    st.dataframe(hist)
except Exception as e:
    st.error(f"Erro ao acessar yfinance: {e}")
