# Análise Exploratória de Dados (AED)
import pandas as pd

df = pd.read_csv('./preparacao_dados/clientes_tratados_v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

print('Verificação inicial:')
print(df.info())

print('Analise de dados nulos: \n', df.isnull().sum())
print('% de dados nulos: \n', df.isnull().mean() * 100 )
df.dropna(inplace=True)
print('Confirmar remoção de dados nulos: \n', df.isnull().sum().sum())

print('Analise de dados duplicados:\n', df.duplicated().sum())

print('Analise de dados únicos:\n', df.nunique())

print('Estatísticas dos dados:\n', df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head(10).to_string())

df.to_csv('clientes_preparados.csv', index=False)
