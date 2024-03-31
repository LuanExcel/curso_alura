import pandas as pd
import re

# Read the Excel file
file_path = r'C:\Users\Luan\OneDrive\Planilhas de estudos aleatorios\Desafios Excel BI\Excel_BI\Atuais\Excel\Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path,usecols=['Data'])

# Create a function to generate the desired output
def split_case(text):
 chars = re.findall('[a-z]+|[A-Z]+|[0-9]+', text)
 return ', '.join(chars)

# Add the results column and print the uotput
df['My Answer'] = df['Data'].apply(split_case)
print(f'Expected Results:\n{df.iloc[:, [0, 1]]}\n\nMy Results:\n{df.iloc[:, [0, 2]]}')



