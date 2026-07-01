import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_trainee = pd.read_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\dados\dados_climaticos_sp_20_25_limpo.csv')

# versao simplificada
df_trainee = df_trainee.rename(columns={
    'TEMPERATURA MEDIA, DIARIA (AUT)(°C)': 'Temperatura',
    'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)': 'Precipitacao',
    'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)': 'Umidade',
    'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)': 'Vento'
})

# checando criterio para regressao linear -> covariancia [temperatura X precipitacao] positiva
cov_temp_precip = df_trainee['Temperatura'].cov(df_trainee['Precipitacao'])
print(cov_temp_precip) # 2.175 -> atende o requisito