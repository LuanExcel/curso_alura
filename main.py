#Esta linha importa a biblioteca pandas, que é frequentemente usada para manipulação e análise de dados em Python.
import pandas as pd
import plotly.express as px

#Nesta linha, é definido o caminho para o arquivo Excel a ser lido. O r antes das 
# aspas indica uma "string bruta" em Python, o que significa que os 
# caracteres de escape dentro da string não serão interpretados
file_path = r'C:\Users\Luan\Projetos_PY\Alura\arquivo\Exemplo.xlsx'

#Esta linha lê o arquivo Excel especificado (file_path) e 
# carrega-o em um DataFrame do pandas.
df = pd.read_excel(file_path,sheet_name="fato")
df = df[['ID','Qtd','Vlr Unit']].copy()

df_dimensao = pd.read_excel(file_path,sheet_name="dimensao")

#sempre referencia o dataframe ja q estou sempre atualizando ele com novos valores
# o fato de sempre usar o .copy() é q sempre que estou manipulando o df ele vai apagar o anterir e salvar esse novo em tela

#
df = df.rename(columns={'ID':"ID_PRODUTO"}).copy()

#essa multiplicação é referente a uma nova coluna
#calculo
df['multiplicacao'] = df['Qtd'] * df['Vlr Unit'] 

#1 - no merge o primeiro arqugumento é a matriz de dimensao
#2 - coluna chave da fato
#3 - coluna chave da dimensao
#4 - a nova coluna vir a esquerda
#procv
df = df.merge(df_dimensao,left_on='ID_PRODUTO',right_on='ID',how='left')

#excluir coluna
df = df.drop(columns=['ID']).copy()

#tranforma todas as colunas de numero em decimal com duas casas decimais {:.2f}
pd.options.display.float_format='{:.2f}'.format

#altero o tipo de dado da coluna para inteiro
df['Qtd'] = df['Qtd'].astype(int)

df = df.rename(columns={'Qtd':'Quantidade'})


df['resultado']= df['multiplicacao'].apply(lambda x: 'subiu' if x >= 10 else ('Desceu' if x < 10 else 'estavel'))

#cria uma coluna com o valor mínimo da coluna indicada
df['min'] = df['multiplicacao'].min()
df['max'] = df['multiplicacao'].max()

# o mean aquivale a media e a median a mediana
df['media'] = df['multiplicacao'].mean()
df['mediana'] = df['multiplicacao'].median()

#cria uma nova coluna vendo na coluna resultado quem é 'subiu' e tira o valor minimo correspondente ao campo multiplicacao
df['teste'] = df[df['resultado'] == 'subiu']['multiplicacao'].min()


#creie um novo DataFrame agrupei pela coluna resultado e usando o calculo de soma na coluna multiplicacao e usei 
# reset_index para considerar o df_agrupar como um novo dataframe
df_agrupar = df.groupby('resultado')['multiplicacao'].sum().reset_index()

fig = px.bar(df_agrupar,x='resultado',y='multiplicacao',text='multiplicacao',title='valor')
fig.show()

pizza = px.pie(df_agrupar,values='multiplicacao',names='resultado')
pizza.show()
  
    
#print(df_agrupar)





