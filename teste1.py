import pandas as pd
import re

# Ler o arquivo Excel
file_path = r'C:\Users\Luan\OneDrive\Planilhas de estudos aleatorios\Desafios Excel BI\Excel_BI\Atuais\Excel\Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path, usecols=['Data'])

# Função para gerar a saída desejada
def split_case(text):
    chars = re.findall('[a-z]+|[A-Z]+|[0-9]+', text)
    return ', '.join(chars)

# Adicionar a coluna de resultados e imprimir a saída
df['My Answer'] = df['Data'].apply(split_case)

# Imprimir as colunas 'Data' e 'My Answer'
print(f'Expected Results:\n{df[["Data", "My Answer"]]}')
