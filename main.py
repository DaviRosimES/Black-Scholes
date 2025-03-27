from src.blacksholes import BlackScholes
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


def main():
    # Título
    st.title('📈 Black-Scholes Option Pricing')

    # Fórmula do Modelo Black-Scholes
    st.subheader("📖 Fórmula do Modelo Black-Scholes")
    st.latex(r"C = S_0 N(d_1) - Ke^{-rT} N(d_2)")
    st.latex(r"P = Ke^{-rT} N(-d_2) - S_0 N(-d_1)")

    # Entradas do usuário
    st.sidebar.header("Parâmetros de Entrada")

    S = st.sidebar.slider('Stock Price', min_value=50, max_value=200, value=100)
    K = st.sidebar.slider('Strike Price (K)', min_value=50, max_value=200, value=100)
    T = st.sidebar.slider('Time to Maturity (T in years)', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    r = st.sidebar.slider('Risk-Free Rate (r)', min_value=0.01, max_value=0.1, value=0.05, step=0.01)
    sigma = st.sidebar.slider('Volatility (σ)', min_value=0.1, max_value=1.0, value=0.2, step=0.05)

    S, K, T, r, sigma = map(float, [S, K, T, r, sigma])
    call_price, put_price = BlackScholes.calculate_price(S, K, T, r, sigma)

    # Criar DataFrame formatado
    df = pd.DataFrame({"Opção": ["Call", "Put"], "Preço": [call_price, put_price]})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
                <div style="padding:15px; border-radius:10px; background-color:#d4edda; text-align:center;">
                    <h3 style="color:#155724;">Call Price</h3>
                    <p style="font-size:24px; font-weight:bold; color:#155724;">{call_price:.2f}</p>
                </div>
                """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
                <div style="padding:15px; border-radius:10px; background-color:#f8d7da; text-align:center;">
                    <h3 style="color:#721c24;">Put Price</h3>
                    <p style="font-size:24px; font-weight:bold; color:#721c24;">{put_price:.2f}</p>
                </div>
                """,
            unsafe_allow_html=True
        )
    bar_chart(df=df)
    vol_chart(S, K, T, r, sigma)


def bar_chart(df):
    # Gráfico de barras comparando os preços
    fig_bar = px.bar(df, x="Opção", y="Preço", color="Opção",
                     color_discrete_map={"Call": "green", "Put": "red"},
                     title="Comparação de Preços: Call vs Put",
                     text="Preço")

    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(yaxis_title="Preço da Opção")

    st.plotly_chart(fig_bar)

def vol_chart(S, K, T, r, s):
    # Gráfico com o impacto da volatilidade nos preços
    sigma_values = np.linspace(0.1, 1, 50)
    call_prices = [BlackScholes.calculate_price(S, K, T, r, s)[0] for s in sigma_values]
    put_prices = [BlackScholes.calculate_price(S, K, T, r, s)[1] for s in sigma_values]

    df_volatility = pd.DataFrame({"Volatilidade": sigma_values, "Call Price": call_prices, "Put Price": put_prices})

    fig_line = px.line(df_volatility, x="Volatilidade", y=["Call Price", "Put Price"],
                       labels={"value": "Preço da Opção", "variable": "Tipo de Opção"},
                       title="Impacto da Volatilidade nos Preços",
                       color_discrete_map={"Call Price": "green", "Put Price": "red"})

    st.plotly_chart(fig_line)

if __name__ == '__main__':
    main()
