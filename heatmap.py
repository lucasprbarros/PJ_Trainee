import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_trainee = pd.read_csv(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\dados_climaticos_sp_20_25_limpo.csv')

df_num = df_trainee.select_dtypes(include='number')

matriz_correlacao = df_num.corr(method='pearson')
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação dos Dados Climáticos de São Paulo')

plt.savefig(r'C:\Users\lupba\OneDrive\Desktop\PJ_Trainee\heatmap_correlacao.png', bbox_inches='tight')

plt.show()