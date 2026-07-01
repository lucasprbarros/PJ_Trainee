import pandas as pd
import matplotlib.pyplot as plt

# carregando os dados (usando a lógica de renomeação do seu script de regressão)
df = pd.read_csv(r'C:\Users\Felipe\OneDrive\Área de Trabalho\FEA Dev\vscode\ultimo hackathon\dados_climaticos_sp_20_25_limpo.csv')

# renomeando colunas para facilitar a manipulação
df = df.rename(columns={
    'TEMPERATURA MEDIA, DIARIA (AUT)(°C)': 'Temperatura',
    'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)': 'Precipitação'
})

# preparação temporal
df['Data Medicao'] = pd.to_datetime(df['Data Medicao'])
df.set_index('Data Medicao', inplace=True)
df = df[['Temperatura', 'Precipitação']].dropna() 

# visualização
fig, ax1 = plt.subplots(figsize=(14, 7))

# temperatura (eixo Y esquerdo)
color_temp = 'tab:red'
ax1.set_ylabel('Temperatura Média (°C)', color=color_temp, fontsize=12)
ax1.plot(df.index, df['Temperatura'], color=color_temp, alpha=0.5, label='Temperatura')
ax1.tick_params(axis='y', labelcolor=color_temp)

# precipitação (eixo Y direito)
ax2 = ax1.twinx()
color_precip = 'tab:blue'
ax2.set_ylabel('Precipitação (mm)', color=color_precip, fontsize=12)
ax2.bar(df.index, df['Precipitação'], color=color_precip, alpha=0.3, label='Precipitação')
ax2.tick_params(axis='y', labelcolor=color_precip)

plt.title('Série Temporal: Temperatura vs Precipitação (São Paulo)', fontsize=14)
fig.tight_layout()
plt.show()