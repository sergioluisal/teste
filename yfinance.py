import streamlit as st
import yfinance as yf

st.title("Teste de yfinance")

ticker = "AAPL"
try:
    dados = yf.Ticker(ticker).history(period="5d")
    if dados.empty:
        st.warning("Nenhum dado encontrado.")
    else:
        st.success("Dados obtidos com sucesso!")
        st.dataframe(dados)
except Exception as e:
    st.error(f"Erro: {e}")

