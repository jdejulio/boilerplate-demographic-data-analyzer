import pandas as pd
import numpy as np


csv_file = "adult.data.csv"
df = pd.read_csv(csv_file)

    # What country has the highest percentage of people that earn >50K?
    ##se calcula el salario máximo: ">50K"
max_salary = df["salary"].max()

    ##se extraen las filas con valor igual a max_salary
lines_max_salary = df[df["salary"] == max_salary]
highest_earning_country = lines_max_salary['native-country'].value_counts().idxmax()

highest_earning_country_percentage = round(len(df[(df["native-country"] == highest_earning_country) & (df["salary"] == max_salary)]) / len(df["native-country"] == highest_earning_country) * 100)
########################
#########CHATGPT########
########################

porcentaje_mayor_50k_por_pais = df[df['salary'] == '>50K'].groupby('native-country')['native-country'].count() / df.groupby('native-country')['native-country'].count() * 100

# Imprimir los resultados
print("Porcentaje de ciudadanos por país que ganan '>50K':")
print(porcentaje_mayor_50k_por_pais.idxmax())
#EXPLICACIÓN DE CHATGPT#

''''df[df['salary'] == '>50K']: Este primer paso filtra el DataFrame original (df) 
para incluir solo las filas donde la columna 'salary' tiene el valor '>50K'. 
Esto crea un nuevo DataFrame que contiene solo las filas con salarios mayores a $50,000.
.groupby('native-country')['native-country'].count(): A continuación, usamos el método 
groupby para agrupar las filas por la columna 'native-country' y luego contamos el número 
de filas en cada grupo utilizando count(). Esto nos dará un objeto Series que tiene como 
índice los países y como valores el número de filas correspondientes a cada país donde el salario es '>50K'.
/ df.groupby('native-country')['native-country'].count(): Dividimos cada valor en 
la serie resultante (número de filas con salario '>50K' por país) por el número total 
de filas por país, que se obtiene mediante df.groupby('native-country')['native-country'].count(). 
Esta división se realiza elemento a elemento y produce una serie con los porcentajes de ciudadanos 
con salario '>50K' por país.

* 100: Multiplicamos cada valor en la serie resultante por 100 para expresar los porcentajes como números enteros.

En resumen, la expresión completa realiza una serie de operaciones para calcular 
el porcentaje de ciudadanos en cada país que tienen un salario '>50K' en relación con 
el número total de ciudadanos por país. Cada paso contribuye a la creación de esta serie de porcentajes.'''