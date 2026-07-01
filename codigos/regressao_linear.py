import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

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

df_trainee = df_trainee[['Temperatura', 'Precipitacao']].dropna()
# somente essas duas colunas serao usadas, .dropna() para evitar erros com sklearn

x = df_trainee[['Temperatura']].values 
y = df_trainee['Precipitacao'].values

model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"slope: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

plt.figure(figsize=(8,6))
plt.scatter(x, y, alpha=0.4, label='Dados reais')
plt.plot(x, y_pred, color='red', linewidth=2, label='Reta de regressão')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Precipitação (mm)')
plt.title('Regressão Linear: Temperatura × Precipitação')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\graficos_tabelas/regressao_temp_precip.png', bbox_inches='tight')
plt.show()