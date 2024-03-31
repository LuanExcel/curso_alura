import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dados = yf.download('PETR4.SA',start='2023-01-01',end='2023-12-31')

#Ao usar dados.columns ele me passa o nome de todas as colunas e ao fornecer uma lista
# com outros nomes ele ja reconhecer e substituie todos os nomes dos campos pelo identificados nessa lista abaixo
dados.columns = ['Abertura','Maximo','Minimo','Fechamento','Fech_Ajuste','Volume']

# raname_axis é responsavel por mudar o nome apenas da coluna 
# indice que no caso desse dataframe é Date e mudou pra Data
dados = dados.rename_axis('Data')

#Pega a coluna q vai usar no grafico inserindo a função plot e aproveitando
#usa o parametro figsize para definir tamanho e largura 
dados['Fechamento'].plot(figsize=(10,6))

#aqui chama o plt q é a biblioteca do matplotlib mudando o nome do titulo do grafico usando o title
plt.title('Variacao do preço por data',fontsize=16)

#adicionando legenda
plt.legend(['Fechamento'])

#aqui traz apenas 60 linhas do dataframe
df = dados.head(60).copy()

#crio uma coluna de Chamada Data duplicando a coluna index q é a Data
df['Data'] = df.index

# E nessa coluna Data aplicao mdates q faz parte do matplotlib.dates e date2num é o mesmo que  DateTo.Number do M
df['Data'] = df['Data'].apply(mdates.date2num)

#print(df)
#plt.show()   
#print(dados)

dados_novo = yf.download('PETR4.SA',start='2023-01-01',end='2023-12-31')


mpf.plot(dados_novo.head(30) ,type='candle',figsize=(16,8),volume=True,mav=(7,14),style='yahoo')

