import streamlit as st

st.title("Explicação sobre o desafio da Asimov Academy - Ecommerce")
'''
O desafio da Asimov Academy envolve uma série de dados fictícios sobre uma empresa para poder testar as
habilidades em Machine Learning. Nesse dataframe disponibilizado são encontrados as variáveis:
* Email	
* Address	
* Avatar	
* Avg. Session Length	
* Time on App	
* Time on Website	
* Length of Membership	
* Yearly Amount Spent
O objetivo do desafio é: Verificar se a empresa deve concentrar seus esforços em aplicativos móveis ou em seu site. 

O desafio pede o modelo de Regressão linear. Que consiste na equação:

y = β0 + β1 * x1 + β2 * x2 + ... + βn * xn
* y = Variável alvo
* β0 = Intercepto (O valor das variáveis independentes quando são igual a 0)
* β1, β2, a βn = Os coeficientes das variáveis independentes. Direção e impacto de cada variável.
* x1, x2, a xn = As variáveis independentes. Dados de entrada.

y = β0 + β1 * (Avg. Session Length) + β2 * (Time on App) + β3 * (Time on Website) + β4 * (Length of Membership)  
'''

st.title("Objetivo do app")
'''Meu objetivo é criar um app com stramlit e python usando os seguintes passos.

1) EDA (Análise exploratória de dados) - para poder tratamento dos dados, remoção de dados ausentes, estabelecer comparações visuais, 
identificar outliers, distribuição dos dados de cada variável e descobrir correlações.

2) Modelo de Machine Learning de Regressão Linear para poder tirar conclusões com base nos resultados dos coeficientes.

3) Criar um simulador de resultados usando o resultado dos coeficientes, encontrados com o modelo de Machine Learnin, onde
você vai poder prever a variável alvo 'Yearly Amount Spent'.
'''

st.title("Resultados:")
'''
O resultado dos coeficientes de Regressão Linear foram:
* Avg. Session Length = 25.72425621  
* Time on App = 38.59713548
* Time on Website = 0.45914788
* Length of Membership = 61.67473243

Isso indica que a empresa deve se concentrar em app e não muito em seu site. A cada 1un. de tempo no app 'Time on App' tem um aumento de 38.59 no gasto do cliente 'Yearly Amount Spent'.
A empresa deve focar estratégias para aumentar as variáveis: 'Length of Membership' e 'Time on App'
'''

st.title("Avaliação do modelo:")
'''
Usando scatterplot para comparar dados reais e previsões
plt.scatter(y_test, y_pred)

MAE
* Todas as predições - valor de teste = valor (Média desse valor)
* Resultado: 7.22 (Os dados fictícios, por isso o valor tão baixo! Modelo quase perfeito...)

MSE
* Ao elevar ao quadrado, teremos um peso MAIOR a erros MAIORES
* No geral, a ideia é penalizar erros 'grosseiros'
* Resultado: 79.81 (Note que ao elevar ao quadrado perdemos a comparação com a variável 'y')

RMSE
* Ao tirar a raíz quadrada (RMSE) conseguimos trazer o resultado do MSE de volta à mesma unidade da variável dependente 'y'
* Facilita a visualização do erro
* Resultado: 8.93 (Maior que o MAE...)

Visualizando a distribuição de resíduos
sns.distplot((y_test-y_pred), bins=50)
* A distribuição é normal
* Podendo seguir sem ajustar ou mudar o modelo
'''
