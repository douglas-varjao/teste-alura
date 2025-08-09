import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df= pd.read_csv('data/dados_imoveis.csv')
df.head()

print(df.info())
print(df.describe())

#exemplo de grafico
sns.pairplot(df)
plt.savefig('imagens/distribuicoes.png')

#remover colunas irrelevantes
df = df[['area', 'quartos', 'banheiros', 'vagas', 'preco']]

#tratar valores nulos
df = df.dropna()

#separar variaveis
x = df.drop('preco', axis=1)
y = df['preco']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

#Metricas

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse:.2f}')
print(f'R²: {r2:.2f}')

#Plot das previsões

plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred)
plt.xlabel('Preço Real')
plt.ylabel('Preço Previsto')
plt.title('Previsão vs Real')
plt.savefig('imagens/scatterplot_predicoes.png')
plt.show()
