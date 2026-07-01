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

colunas_principais = ['Temperatura', 'Precipitacao', 'Umidade', 'Vento']
df_num = df_trainee[colunas_principais]

matriz_correlacao = df_num.corr(method='pearson')
plt.figure(figsize=(6, 5))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação dos Dados Climáticos de São Paulo')

plt.savefig(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\graficos_tabelas\heatmap_correlacao_simplificado.png', bbox_inches='tight')
plt.show()