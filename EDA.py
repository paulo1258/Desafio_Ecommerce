import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

caminho = "paulo1258/Desafio_Ecommerce/ecommerce-customers"

df = pd.read_csv(caminho)

df1 = df.drop(['Avatar', 'Address', 'Email'], axis=1)

df_col = df1.select_dtypes(include=[np.number])

st.title("Análise de um ecommerce")

'''
DESAFIO:
Trabalharemos com o arquivo csv do Ecommerce Customers da empresa. Possui informações do cliente, como Email, Endereço e sua cor Avatar. Em seguida, ele também possui colunas de valores numéricos:.

* Avg. Session Length: Tempo médio das sessões de consultoria de estilo na loja.
* Time on App: tempo médio gasto no app em minutos.
* Time on Website: tempo médio gasto no site em minutos.
* Lenght of Membership: Há quantos anos o cliente é membro.
'''

st.header("Jointplot entre Time On Website - scatterplot + histograma")
'''
Jointplot é um gráfico da biblioteca seaborn que permite criar um gráfico bivariado combinando um gráfico de dispersão ou outro tipo com gráficos univariados marginais

* Podemos verificar a distribuição de dados e a correlação entre as variáveis.
* Nesse caso, usei um for loop para iterar com as variáveis onde o 'Yearly Amount Spent' é o eixo 'y' (Variável alvo) e o restante é 'x' 
* Podemos verificar correlações positivas entre as variáveis.
    - 'Yearly Amount Spent' x 'Length of Membership' (Alta)
    - 'Yearly Amount Spent' x 'Time on App'
    - 'Yearly Amount Spent' x 'Avg. Session Lenght'
* Também a presença de outliers em todos os gráficos, especialmente em:
    - 'Yearly Amount Spent' x 'Time on App'
    - 'Yearly Amount Spent' x 'Avg. Session Lenght'
'''

for col in df_col:
    if col != 'Time on Website':
        # Criando uma nova figura para cada gráfico
        fig = sns.jointplot(x=col, y='Yearly Amount Spent', data=df1, kind='scatter')
        # Exibindo o gráfico no Streamlit
        st.pyplot(fig)

st.header("Jointplot entre Time On Website - Scatterplot hex")
'''
O Scatterplot Hexagonal é uma variação do gráfico de dispersão, os pontos são agrupados em hexágonos e 
a cor ou intensidade de cada hexágono representa o número de pontos ou a densidade de pontos dentro daquela área.

* Podemos verificar uma contagem de pontos alta no meio do gráfico
    * Indicando maior densidade de pontos
'''

joint_plot = sns.jointplot(x='Time on App', y='Length of Membership', data=df1, kind='hex')

st.pyplot(joint_plot.fig)

st.header("Pairplot - Histograma + scatterplot")
'''
Usei o Pairplot para criar uma matriz onde podemos comparar todas as variáveis criando gráficos de dispersão e histograma.
* Facilita a visualização da distribuição dos dados e a correlação entre as variáveis.
'''
pair_plot = sns.pairplot(data=df1, kind='scatter', diag_kind='hist')

st.pyplot(pair_plot)

st.header("Matriz de correlção entre as variáveis")

'''
A matriz de correlação foi feita com a função .corr() que por padrão usa a correlação de Pearson, variando de -1 a 1
* Correlação de Pearson: Mede a força e a direção de uma relação linear entre duas variáveis
    * 1 = correlação linear perfeita
    * 0 = ausência de correlação linear 
    * -1 = correlação linear negativa perfeita
'''
df_corr = df.select_dtypes(include=[np.number])

df_corr1 = df_corr.corr()

df_corr1

'''
Como podemos verificar as variáveis que tem maior correlação é 'Yearly Amount Spent' e 'Length of Membership com 0.8091
'''

st.header("Lmplot - Analisando a correlação entre 'Yearly Amount Spent' e 'Length of Membership")
'''
Lmplot permite ver a reta da regressão linear ajustada aos dados de dispersão
'''
lm_plot = sns.lmplot(data=df1, x='Yearly Amount Spent', y='Length of Membership')

st.pyplot(lm_plot)

'''

'''
