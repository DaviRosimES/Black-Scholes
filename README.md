# Black-Scholes Option Pricing

Este projeto implementa um aplicativo interativo para precificação de opções usando o modelo Black-Scholes. O aplicativo permite que os usuários insiram parâmetros financeiros e visualizem os preços das opções de compra (Call) e venda (Put) de forma dinâmica.

## 🚀 Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Streamlit**: Para criação da interface interativa e deploy.
- **Plotly**: Para geração de gráficos interativos.
- **NumPy e Pandas**: Para manipulação de dados.

## 📖 Como Funciona
O modelo Black-Scholes é uma fórmula matemática utilizada para calcular o preço teórico de opções. A fórmula utilizada no aplicativo é:


<p align="center">
$$C = S_0 N(d_1) - Ke^{-rT} N(d_2)$$
</p>

<p align="center">
$$P = Ke^{-rT} N(-d_2) - S_0 N(-d_1)$$
</p>

Onde:
- \( C \) e \( P \) são os preços das opções Call e Put.
- \( S_0 \) é o preço do ativo.
- \( K \) é o preço de strike da opção.
- \( T \) é o tempo até o vencimento.
- \( r \) é a taxa de juros livre de risco.
- \( \sigma \) é a volatilidade do ativo.
- \( N(d) \) é a função de distribuição acumulada da normal.

## 🛠️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/DaviRosimES/Black-Scholes.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd Black-Scholes
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o aplicativo:
   ```bash
   streamlit run main.py
   ```

## 📊 Funcionalidades
✅ Entrada de parâmetros via barra lateral (preço do ativo, strike, tempo, taxa de juros e volatilidade).  
✅ Cálculo dos preços das opções Call e Put.  
✅ Exibição de resultados estilizados com HTML e CSS.  
✅ Gráficos interativos do impacto da volatilidade nos preços das opções.  
✅ Deploy feito utilizando **Streamlit Cloud**.

## 🌎 Deploy
O aplicativo está disponível online via **Streamlit Cloud**. Para acessá-lo, clique no link:
👉 [Deploy do projeto](https://blacksholesdr.streamlit.app/)
