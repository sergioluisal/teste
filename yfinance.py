import streamlit as st
import yfinance as yf

st.title("Teste de Conexão com Yahoo Finance (via yfinance)")

ticker = st.text_input("Digite o ticker (ex: AAPL, MSFT, PETR4.SA):", "AAPL")

if ticker:
    try:
        st.write(f"Buscando dados para: {ticker}")
        dados = yf.Ticker(ticker).history(period="5d")

        if dados.empty:
            st.error(f"Nenhum dado retornado para '{ticker}'. Verifique o símbolo.")
        else:
            st.success(f"Dados obtidos com sucesso para {ticker}!")
            st.dataframe(dados)
    except Exception as e:
        st.error(f"Erro ao tentar obter os dados: {e}")
