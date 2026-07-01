import pandas as pd
# tabela de momentos estatisticos

df_trainee = pd.read_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\dados\dados_climaticos_sp_20_25_limpo.csv')

colunas = ['PRECIPITACAO TOTAL, DIARIO (AUT)(mm)', 'PRESSAO ATMOSFERICA MEDIA DIARIA (AUT)(mB)', 'TEMPERATURA DO PONTO DE ORVALHO MEDIA DIARIA (AUT)(°C)', 'TEMPERATURA MAXIMA, DIARIA (AUT)(°C)', 'TEMPERATURA MEDIA, DIARIA (AUT)(°C)', 'TEMPERATURA MINIMA, DIARIA (AUT)(°C)', 'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)', 'UMIDADE RELATIVA DO AR, MINIMA DIARIA (AUT)(%)', 'VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)', 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)']

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

tabela_momentos = pd.DataFrame(resultados).T.round(2)

tabela_momentos.to_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\graficos_tabelas\tabela_momentos.csv')

print(tabela_momentos)