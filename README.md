# scatterplot

- English -

Sure! Let me explain the Python code step by step:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
```

- `import numpy as np`: Imports the NumPy library with the alias `np`. NumPy is a library for numerical computing in Python. It provides support for arrays and matrices, along with mathematical functions to operate on these arrays.
  
- `import matplotlib.pyplot as plt`: Imports the Matplotlib library with the alias `plt`. Matplotlib is a library for creating plots in Python. `matplotlib.pyplot` provides an interface for creating figures and axes in Python.
  
- `from scipy.stats import pearsonr`: Imports the `pearsonr` function from the SciPy library. The `pearsonr` function is used to calculate the Pearson correlation coefficient between two variables.

```python
# Generating random data with a non-linear relationship
np.random.seed(0)
price_euro = np.random.randint(10, 100, size=50)
price = price_euro * 1.18  # Converting to Euros
units_sold = 1000 / (price + np.random.normal(scale=10, size=50))
```

- `np.random.seed(0)`: Sets a seed to ensure that the randomly generated numbers are the same in all code executions. This makes the results reproducible.

- `price_euro = np.random.randint(10, 100, size=50)`: Generates 50 random integers between 10 and 100, representing the price of the products in Euros.

- `price = price_euro * 1.18`: Converts the prices to Euros by multiplying them by 1.18.

- `units_sold = 1000 / (price + np.random.normal(scale=10, size=50))`: Generates the number of units sold for each price. The relationship between price and units sold is non-linear. The number of units sold is calculated as 1000 divided by the price plus a normally distributed random value with mean zero and standard deviation 10.

```python
# Calculating the correlation coefficient
corr, _ = pearsonr(price, units_sold)
```

- `corr, _ = pearsonr(price, units_sold)`: Calculates the Pearson correlation coefficient between price and units sold. The correlation coefficient measures the strength and direction of the linear relationship between two variables. Here, we are interested in the correlation between the product price and the number of units sold.

```python
# Creating the scatter plot with trend line
plt.figure(figsize=(8, 6))
plt.scatter(price, units_sold, color='blue', alpha=0.5)
plt.plot(np.unique(price), np.poly1d(np.polyfit(price, units_sold, 2))(np.unique(price)), color='red')
```

- `plt.figure(figsize=(8, 6))`: Creates a new figure with the specified size (width: 8 inches, height: 6 inches).

- `plt.scatter(price, units_sold, color='blue', alpha=0.5)`: Creates a scatter plot of prices versus units sold. Each point on the plot represents a pair of values (price, units sold).

- `plt.plot(np.unique(price), np.poly1d(np.polyfit(price, units_sold, 2))(np.unique(price)), color='red')`: Adds a trend line to the scatter plot. The trend line is fitted using a second-degree polynomial to the data.

```python
# Adding labels and title
plt.title(f'Relationship between Price and Units Sold (Correlation: {corr:.2f})')
plt.xlabel('Price (€)')
plt.ylabel('Units Sold')

# Displaying the plot
plt.grid(True)
plt.show()
```

- `plt.title(f'Relationship between Price and Units Sold (Correlation: {corr:.2f})')`: Adds a title to the plot that includes the correlation coefficient between price and units sold.

- `plt.xlabel('Price (€)')`: Adds a label to the x-axis indicating that prices are in Euros.

- `plt.ylabel('Units Sold')`: Adds a label to the y-axis indicating that units sold are the number of units sold.

- `plt.grid(True)`: Adds grid lines to the plot.

- `plt.show()`: Displays the plot.

I hope this clarifies how the code works! If you have any further questions, feel free to ask!

- Português -
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


