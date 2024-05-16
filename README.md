# scatterplot
Claro! Vou explicar o código Python passo a passo:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
```

- `import numpy as np`: Importa a biblioteca NumPy com o alias `np`. NumPy é uma biblioteca para computação numérica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operar nesses arrays.
  
- `import matplotlib.pyplot as plt`: Importa a biblioteca Matplotlib com o alias `plt`. Matplotlib é uma biblioteca para criação de gráficos em Python. `matplotlib.pyplot` fornece uma interface para criar figuras e eixos em Python.
  
- `from scipy.stats import pearsonr`: Importa a função `pearsonr` da biblioteca SciPy. A função `pearsonr` é usada para calcular o coeficiente de correlação de Pearson entre duas variáveis.

```python
# Gerando dados aleatórios com relação não-linear
np.random.seed(0)
preco_euro = np.random.randint(10, 100, size=50)
preco = preco_euro * 1.18  # Convertendo para Euros
unidades_vendidas = 1000 / (preco + np.random.normal(scale=10, size=50))
```

- `np.random.seed(0)`: Define uma semente para garantir que os números aleatórios gerados sejam os mesmos em todas as execuções do código. Isso torna os resultados reproduzíveis.

- `preco_euro = np.random.randint(10, 100, size=50)`: Gera 50 números inteiros aleatórios entre 10 e 100, representando o preço dos produtos em Euros.

- `preco = preco_euro * 1.18`: Converte os preços para Euros multiplicando-os por 1.18.

- `unidades_vendidas = 1000 / (preco + np.random.normal(scale=10, size=50))`: Gera o número de unidades vendidas para cada preço. A relação entre o preço e as unidades vendidas é não-linear. O número de unidades vendidas é calculado como 1000 dividido pelo preço mais um valor aleatório normalmente distribuído com média zero e desvio padrão 10.

```python
# Calculating the correlation coefficient
corr, _ = pearsonr(preco, unidades_vendidas)
```

- `corr, _ = pearsonr(preco, unidades_vendidas)`: Calcula o coeficiente de correlação de Pearson entre o preço e as unidades vendidas. O coeficiente de correlação mede a força e a direção da relação linear entre duas variáveis. Aqui, estamos interessados na correlação entre o preço do produto e o número de unidades vendidas.

```python
# Criando o gráfico de dispersão com linha de tendência
plt.figure(figsize=(8, 6))
plt.scatter(preco, unidades_vendidas, color='blue', alpha=0.5)
plt.plot(np.unique(preco), np.poly1d(np.polyfit(preco, unidades_vendidas, 2))(np.unique(preco)), color='red')
```

- `plt.figure(figsize=(8, 6))`: Cria uma nova figura com o tamanho especificado (largura: 8 polegadas, altura: 6 polegadas).

- `plt.scatter(preco, unidades_vendidas, color='blue', alpha=0.5)`: Cria um gráfico de dispersão dos preços versus as unidades vendidas. Cada ponto no gráfico representa um par de valores (preço, unidades vendidas).

- `plt.plot(np.unique(preco), np.poly1d(np.polyfit(preco, unidades_vendidas, 2))(np.unique(preco)), color='red')`: Adiciona uma linha de tendência ao gráfico de dispersão. A linha de tendência é ajustada usando um polinômio de segundo grau aos dados.

```python
# Adicionando rótulos e título
plt.title(f'Relationship between Price and Units Sold (Correlation: {corr:.2f})')
plt.xlabel('Price (€)')
plt.ylabel('Units Sold')

# Exibindo o gráfico
plt.grid(True)
plt.show()
```

- `plt.title(f'Relationship between Price and Units Sold (Correlation: {corr:.2f})')`: Adiciona um título ao gráfico que inclui o coeficiente de correlação entre o preço e as unidades vendidas.

- `plt.xlabel('Price (€)')`: Adiciona um rótulo ao eixo x indicando que os preços estão em Euros.

- `plt.ylabel('Units Sold')`: Adiciona um rótulo ao eixo y indicando que as unidades vendidas são o número de unidades vendidas.

- `plt.grid(True)`: Adiciona linhas de grade ao gráfico.

- `plt.show()`: Exibe o gráfico.

Espero que isso esclareça como o código funciona! Se tiver mais alguma dúvida, estou à disposição para ajudar!
