import numpy as np

# Se utiliza una Simulacion para replicar computacionalmente el lanzamiento de una moneda 
# Simular 10 lanzamientos de una moneda con "A" (Águila/Cara) y "S" (Sol/Cruz)
lanzamientos_10 = np.random.choice(["A", "S"], size=10, replace=True)
print("Lanzamientos:", lanzamientos_10)

# Calcular la secuencia de frecuencias relativas de "A"
frecuencia_acumulada = np.cumsum(lanzamientos_10 == "A")
frecuencia_relativa = np.round(frecuencia_acumulada / np.arange(1, 11), 2) # calcula la frecuencia relativa acumulada y la redondea a 2 decimales.

print("Frecuencia relativa de Águila (Cara) en cada lanzamiento:", frecuencia_relativa)

from scipy.stats import norm

# Calcular la probabilidad acumulada P(X < 3.5) para N(3, 0.5)
probabilidad = norm.cdf(3.5, loc=3, scale=0.5) #La función norm.cdf(x, loc, scale) proviene de scipy.stats y se usa para calcular la función de distribución acumulada (CDF, Cumulative Distribution Function) de una distribución normal.
print("P(X < 3.5):", probabilidad)

import matplotlib.pyplot as plt

# Generar 100 números con distribución normal N(10, 1)
x = np.random.normal(loc=10, scale=1, size=100)

# Calcular la media
promedio = np.mean(x)
print("Promedio:", promedio)

# Histograma de frecuencias absolutas
plt.hist(x, bins=10, edgecolor="black")
plt.title("Histograma de frecuencias absolutas")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de caja y bigotes
plt.boxplot(x, vert=False)
plt.title("Gráfico de caja y bigotes")
plt.show()
# El Historigrama es un tipo de grafico que nos permite visualizar la distribución de los datos, en este caso se muestra la frecuencia de los datos generados en el eje y y los valores generados en el eje x.
# Histograma con la curva de distribución normal superpuesta
plt.hist(x, bins=10, density=True, alpha=0.6, color="b", edgecolor="black")
x_values = np.linspace(min(x), max(x), 100)
plt.plot(x_values, norm.pdf(x_values, loc=10, scale=1), color="red", linewidth=2)
plt.title("Histograma con curva normalizada")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.show()

from scipy.stats import binom

# Volvemos a generar 20 valores con distribución binomial (éxito=1, fracaso=0)
x = np.random.binomial(n=1, p=0.5, size=20)
print("Valores generados:", x)

# Contar éxitos (1) y fracasos (0)
valores, conteo = np.unique(x, return_counts=True)
print("Conteo de éxitos y fracasos:", dict(zip(valores, conteo)))

# Probabilidad de obtener un 1
P = np.sum(x) / len(x)
print("Probabilidad de éxito (1):", P)

# Calcular la probabilidad de obtener 0, 1, 2, 3 o 4 respuestas correctas
probabilidad_acumulada = sum(binom.pmf(k, n=12, p=0.2) for k in range(5))
print("Probabilidad de obtener menos de 4 respuestas correctas:", probabilidad_acumulada)

# Probabilidad de obtener al menos 4 respuestas correctas
probabilidad_al_menos_4 = 1 - probabilidad_acumulada
print("Probabilidad de obtener al menos 4 respuestas correctas:", probabilidad_al_menos_4)


probabilidad_menor_9 = norm.cdf(9, loc=8, scale=2)
print("P(X < 9) para N(8,2):", probabilidad_menor_9)

datos = np.random.normal(loc=5, scale=0.5, size=150)

from scipy.stats import mode
# calculamos la media, mediana y moda de los datos generados
media = np.mean(datos)
mediana = np.median(datos)
moda = mode(datos).mode[0]

print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

# Gráfico de caja y bigotes son utilizados para visualizar la distribución de los datos, 
# en este caso se muestra la distribución de los datos generados.
plt.boxplot(datos, vert=False)
plt.title("Gráfico de caja y bigotes de los datos generados")
plt.show()

plt.hist(datos, bins=10, density=True, alpha=0.6, color="b", edgecolor="black")
x_values = np.linspace(min(datos), max(datos), 100)
plt.plot(x_values, norm.pdf(x_values, loc=5, scale=0.5), color="red", linewidth=2)
plt.title("Histograma con curva normalizada")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.show()
# calculamos la probabilidad de obtener un valor menor a 5.5
x_binomial = np.random.binomial(n=1, p=0.5, size=30)
# esta funcion nos permite contar los exitos y fracasos
valores_bin, conteo_bin = np.unique(x_binomial, return_counts=True)

print("Conteo de éxitos y fracasos:", dict(zip(valores_bin, conteo_bin)))
# calculamos la probabilidad de obtener un 1
probabilidad_exito = np.sum(x_binomial) / len(x_binomial)
print("Probabilidad de éxito (1):", probabilidad_exito)
