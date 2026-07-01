import pandas as pd

df_trainee = pd.read_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\dados\dados_climaticos_sp_20_25_limpo.csv')

# versao simplificada
df_trainee = df_trainee.rename(columns={
    'TEMPERATURA MEDIA, DIARIA (AUT)(°C)': 'Temperatura',
    'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)': 'Precipitacao',
    'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)': 'Umidade',
    'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)': 'Vento'
})

colunas = ['Temperatura', 'Precipitacao', 'Umidade', 'Vento']

resultados = {}
for col in colunas:
    serie = df_trainee[col].dropna()
    resultados[col] = {
        'media': serie.mean(),
        'mediana': serie.median(),
        'moda': serie.mode()[0],
        'variancia': serie.var(),
        'desvio_padrao': serie.std(),
        'skewness': serie.skew(),
        'kurtosis': serie.kurt()
    }

tabela_momentos_simplificado = pd.DataFrame(resultados).T.round(2)
tabela_momentos_simplificado.to_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\graficos_tabelas\tabela_momentos_simplificada.csv')

print(tabela_momentos_simplificado)