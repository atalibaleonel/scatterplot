import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Gerando dados aleatórios com relação não-linear
np.random.seed(0)
preco_euro = np.random.randint(10, 100, size=50)
preco = preco_euro * 1.18  # Convertendo para Euros
unidades_vendidas = 1000 / (preco + np.random.normal(scale=10, size=50))

# Calculating the correlation coefficient
corr, _ = pearsonr(preco, unidades_vendidas)

# Criando o gráfico de dispersão com linha de tendência
plt.figure(figsize=(8, 6))
plt.scatter(preco, unidades_vendidas, color='blue', alpha=0.5)
plt.plot(np.unique(preco), np.poly1d(np.polyfit(preco, unidades_vendidas, 2))(np.unique(preco)), color='red')

# Adicionando rótulos e título
plt.title(f'Relationship between Price and Units Sold (Correlation: {corr:.2f})')
plt.xlabel('Price (€)')
plt.ylabel('Units Sold')

# Exibindo o gráfico
plt.grid(True)
plt.show()
