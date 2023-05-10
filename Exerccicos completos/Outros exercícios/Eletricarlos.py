import pandas as pd
import plotly.express as px

planilha = pd.read_excel('A.xlsx')

planilha['DATA'] = pd.to_datetime(planilha['DATA'], format='%d/%m/%Y')
planilha = planilha.sort_values(by='DATA')
# planilha.to_excel('A_ordenado.xlsx', index=False)
# print(planilha)
contagem = planilha['AP'].value_counts()
print(contagem)
# grafico=px.histogram(planilha,x='AP', y='DATA')