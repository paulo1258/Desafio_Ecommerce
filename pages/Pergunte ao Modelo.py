import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Exemplo de dados (substitua pelo seu DataFrame real)

caminho = "ecommerce-customers"
df = pd.read_csv(caminho)

df1 = df.drop(['Avatar', 'Address', 'Email'], axis=1)

df_col = df1.select_dtypes(include=[np.number])

# Dividir os dados em conjuntos de treino e teste
x = df1.drop(['Yearly Amount Spent'], axis=1)
y = df1['Yearly Amount Spent']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Treinar o modelo de regressão linear
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# Interface do usuário com Streamlit
st.title("Previsão de Gasto Anual")
st.write("Insira os valores para prever o Gasto Anual:")

# Entradas para os usuários inserirem os valores
avg_session_length = st.number_input("Avg. Session Length", min_value=0.0, value=5.0, step=0.1)
time_on_app = st.number_input("Time on App", min_value=0.0, value=5.0, step=0.1)
time_on_website = st.number_input("Time on Website", min_value=0.0, value=5.0, step=0.1)
length_of_membership = st.number_input("Length of Membership", min_value=0.0, value=5.0, step=0.1)

# Botão para fazer a previsão
if st.button("Prever Gasto Anual"):
    # Fazer a previsão com os valores inseridos
    input_data = np.array([[avg_session_length, time_on_app, time_on_website, length_of_membership]])
    predicted_amount = lin_reg.predict(input_data)[0]
    
    # Exibir a previsão
    st.write(f"**Previsão do Gasto Anual:** ${predicted_amount:.2f}")

    # Exibir os coeficientes do modelo
    coeficientes = lin_reg.coef_
    st.write("**Coeficientes do Modelo:**")
    st.write(f"Avg. Session Length: {coeficientes[0]:.4f}")
    st.write(f"Time on App: {coeficientes[1]:.4f}")
    st.write(f"Time on Website: {coeficientes[2]:.4f}")
    st.write(f"Length of Membership: {coeficientes[3]:.4f}")
