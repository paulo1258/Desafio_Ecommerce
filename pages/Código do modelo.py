import streamlit as st
st.title("Código do modelo de Machine Learning")

code = '''
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

# 1) Separando os dados para a análise:
df1 = df.drop(['Avatar', 'Address', 'Email'], axis=1)

# 2) Somente os dados de números
df_col = df1.select_dtypes(include=[np.number])

# 3) Separando as variáveis em 'x' e 'y' (alvo) 
x = df1.drop(['Yearly Amount Spent'], axis=1)
y = df1['Yearly Amount Spent']

# 4) Separando os dados de treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 5) Instanciando a classe - modelo de regressão linear
lin_reg = LinearRegression()

# 6) 'Fit' ajustando os dados de treino ao modelo de regressão linear
lin_reg.fit(x_train, y_train)

# 7) Criando previsões com os dados de teste
y_pred = model.predict(X_test)

# 8) Verificando os resíduos e se eles são normalmente distribuídos
residuos = y_test - y_pred_test
print(residuos)
sns.histplot(data=residuos, kde=True)

# 9) Verificando os Coeficientes e considerações finais
coeficientes = lin_reg.coef_
print('Coeficientes:', coeficientes)

# 10) Scatterplot para comparar os dados feitos pela previsão x dados reais 
plt.scatter(y_test, y_pred)
xlabel('y_test')
ylabel('y_pred')

# 11) Avaliando o modelo - Medindo o MAE, MSE e RMSE
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MSE): {mae}")
# Todas as predições - valor de teste = valor (Média desse valor)
# Resultado: 7.22 (Os dados fictícios, por isso o valor tão baixo! Modelo quase perfeito...)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")
# Ao elevar ao quadrado, teremos um peso MAIOR a erros MAIORES
# No geral, a ideia é penalizar erros 'grosseiros'
# Resultado: 79.81 (Note que ao elevar ao quadrado perdemos a comparação com a variável 'y')

rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")
# Ao tirar a raíz quadrada (RMSE) conseguimos trazer o resultado do MSE de volta à mesma unidade da variável dependente 'y'
# Facilita a visualização do erro
# Resultado: 8.93 (Maior que o MAE...)

# 12) Visualizar a distribuição dos resíduos
sns.distplot((y_test-y_pred), bins=50)
# A distribuição é normal
# Podendo seguir sem ajustar ou mudar o modelo
'''
st.subheader("Código da Aplicação")
st.code(code, language='python')
