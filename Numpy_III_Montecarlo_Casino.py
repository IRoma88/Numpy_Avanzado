# -*- coding: utf-8 -*-


#Simulacion de MonteCarlo

La simulación de MonteCarlo debe su nombre al famoso casino de Mónaco debido a que la ruleta es el juego de casino más famoso y un mecanismo muy sencillo de generar números aleatorios.

El objetivo principal de la simulación de Montecarlo es intentar imitar el comportamiento de variables reales para, en la medida de lo posible, analizar o predecir cómo van a evolucionar.

En economía, la simulación de Montecarlo se utiliza tanto en empresas como en inversión. Siendo en el mundo de la inversión donde más se utiliza.

Dado que la rentabilidad de una inversión es impredecible, se utiliza este tipo de método para evaluar distintos tipos de escenarios.

##Caso a realizar

Para este ejemplo, intentaremos predecir cuánto dinero debemos presupuestar para las comisiones de ventas para el próximo año. Este problema es útil para el modelado porque tenemos una fórmula definida para calcular las comisiones y probablemente tengamos algo de experiencia con los pagos de comisiones de años anteriores.

Este problema también es importante desde una perspectiva comercial. Las comisiones de ventas pueden ser un gran gasto de venta y es importante planificar adecuadamente este gasto. Además, el uso de una simulación de Monte Carlo es una mejora relativamente simple que se puede realizar para aumentar lo que normalmente es un proceso de estimación poco sofisticado.

En este ejemplo, la comisión de ventas de muestra se vería así para una fuerza de ventas de 5 personas:

|Vendedor|Objetivo Ventas| Ventas reales| % Conseguido|Ratio de Comision|Cantidad de Comision|
---|---|---|---|---|---|
1|100000€|88000|88%|2%|1760€
2|200000€|202000|101%|4%|8080€
3|75000€|90000|120%|4%|3600€
4|400000€|360000|90%|2%|7200€
5|500000€|35000|70%|0%|0€

El ratio de comision se obtiene segun el porcentaje conseguido:

|% ventas conseguid|Ratio de comisión|
|---|---|
|80-90%|2%|
|91-99%|3%|
|>=100%|4%|

Imagina que tu tarea como analista es decirle a finanzas cuánto presupuestar para las comisiones de ventas para el próximo año. Un enfoque podría ser asumir que todos hacen el 100% de su objetivo y ganan la tasa de comisión del 4%.

|Vendedor|Objetivo Ventas| Ventas reales| % Conseguido|Ratio de Comision|Cantidad de Comision|
---|---|---|---|---|---|
1|100000€|100000€|100%|4%|4000€
2|200000€|200000€|100%|4%|8080€
3|75000€|75000€|100%|4%|3000€
4|400000€|400000€|100%|4%|16000€
5|500000€|500000€|100%|4%|20000€

Finanzas te diriía que ya les gustaría que se cumpliese ese escenario, pero que necesitan uno realista. Por lo que decides presentar otras dos opciones:

Opcion 1:

|Vendedor|Objetivo Ventas| Ventas reales| % Conseguido|Ratio de Comision|Cantidad de Comision|
---|---|---|---|---|---|
1|100000€|95000|95%|3%|2850€
2|200000€|204000|102%|4%|8160€
3|75000€|60000|80%|2%|1200€
4|400000€|480000|120%|4%|19200€
5|500000€|40000|80%|2%|8000€

Total: 39410€

Opcion 2:

|Vendedor|Objetivo Ventas| Ventas reales| % Conseguido|Ratio de Comision|Cantidad de Comision|
---|---|---|---|---|---|
1|100000€|10500|105%|4%|4200€
2|200000€|14000|70%|0%|0€
3|75000€|74250|99%|3%|2228€
4|400000€|352000|88%|2%|7040€
5|500000€|55000|110%|4%|22000€

Total:35468€


Esta vez finanzas dice: “este rango es útil, pero ¿cuál es la probabilidad de que se cumpla alguno de estos dos escenarios? Además, necesitamos que haga esto para un equipo de ventas de 500 personas y modele varias tarifas diferentes para determinar la cantidad a presupuestar”.

Este enfoque simple ilustra el método iterativo básico para una simulación de Monte Carlo. Repita este proceso muchas veces para determinar un rango de valores de comisión potenciales para el año. Hacer esto manualmente a mano es un desafío. Afortunadamente, Python hace que este enfoque sea mucho más simple.

En su nivel más simple, un análisis (o simulación) de Monte Carlo implica ejecutar muchos escenarios con diferentes entradas aleatorias y resumir la distribución de los resultados.

Usando el análisis de comisiones, podemos continuar con el proceso manual que comenzamos anteriormente, pero ejecutar el programa 100 o incluso 1000 veces y obtendremos una distribución de los posibles montos de las comisiones. Esta distribución puede informar la probabilidad de que el gasto se encuentre dentro de una determinada ventana. Al final del día, esta es una predicción, por lo que probablemente nunca la predeciremos con exactitud. Podemos desarrollar una idea más informada sobre el riesgo potencial de sub o sobre presupuestar.

Hay dos componentes para ejecutar una simulación de Monte Carlo:

* la ecuacion a evaluar
* las variables aleatorias para la entrada

Para las variables de entrada podemos obserbar los datos históricos en el siguiente grafico donde la x es el % de ventas conseguido y la y es la frecuencia que se ha obtenido dicho porcentaje.

![image.png](data:image/png;base64,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)

Esta distribución parece una distribución normal con una media del 100 % y una desviación estándar del 10 %. Esta información es útil porque podemos modelar nuestra distribución de variables de entrada para que sea similar a nuestra experiencia en el mundo real.

#Recrea los datos históricos usando Numpy
"""
Utiliza la función predeterminada de Numpy np.random.normal para recrear los datos históricos con 500 repeticiones y almacena su resultado en la variable pct_ventas
"""

import numpy as np

avg = 1
std_dev = .1
num_reps = 500

pct_ventas = np.random.normal(avg, std_dev, num_reps).round(2)

print(pct_ventas[:10])

#@title Comprueba los datos historicos generados
import matplotlib.pyplot as plt
np.set_printoptions(formatter={'float_kind':"{:.2f}".format})
list_percent=list(range(70,135,10))
setenta=0
ochenta=0
noventa=0
cien=0
ciendiez=0
cienveint=0
mascientoveint=0
for i in pct_ventas:
  if i<=0.70:
    setenta+=1
  elif i>0.70 and i<=0.80:
    ochenta+=1
  elif i>0.80 and i<=0.90:
    noventa+=1
  elif i>0.90 and i<=1.00:
    cien+=1
  elif i>1.00 and i<=1.10:
    ciendiez+=1
  elif i>1.10 and i<=1.20:
    cienveint+=1
  elif i>1.20:
    mascientoveint+=1
result=[setenta, ochenta, noventa, cien, ciendiez, cienveint,mascientoveint]





# counts=[np.sum(pct_ventas<=70),np.sum(70<pct_ventas and pct_ventas<=80),np.sum(80<pct_ventas and pct_ventas <=90),np.sum(90<pct_ventas and pct_ventas <=100),np.sum(100<pct_ventas and pct_ventas <=110),np.sum(110<pct_ventas and pct_ventas <=120),np.sum(pct_ventas>=120)]

plt.bar([str(z) for z in list_percent], result)

plt.ylabel('Frecuencia')

plt.xlabel('Objetivos de ventas')

plt.title('Usuarios de lenguajes de programación')

plt.show()
def check():
  if pct_ventas.std().round(1)==0.1 and pct_ventas.mean().round(0):
    return 'Datos historicos generados correctos'
  else:
    return 'Los datos históricos generados no son correctos'
check()

"""#Recrea el histórico de objetivos de ventas

Hay otro valor que necesitamos simular y es el objetivo de ventas real. Para ilustrar una distribución diferente, vamos a suponer que la distribución de nuestro objetivo de ventas se parece a esto:

![image.png](data:image/png;base64,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)
Definitivamente no se trata de una distribución normal. Esta distribución nos muestra que los objetivos de ventas se establecen entre 5 posibilidades y la frecuencia es menor a medida que el obtjetivo es más elevado.

Esta distribución podría ser indicativa de un proceso de fijación de objetivos muy simple en el que las personas se agrupan en determinados grupos y se les asignan objetivos de forma coherente en función de su antigüedad, el tamaño del territorio o las ventas conseguidas el año anterior.

Para este ejemplo, utilizaremos una distribución uniforme pero asignaremos tasas de probabilidad más bajas para algunos de los valores.
"""

sales_target_values = [ 100000, 200000, 300000, 400000, 500000]
sales_target_prob = [.6, .2, .1, .05, .05]
num_reps=500
sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)

print(sales_target[:10])

#@title Comprueba los datos históricos de objetivo de ventas

x = sales_target_values
cont100000=0
cont200000=0
cont300000=0
cont400000=0
cont500000=0
for i in sales_target:
  if i==100000:
    cont100000+=1
  elif i==200000:
    cont200000+=1
  elif i==300000:
    cont300000+=1
  elif i==400000:
    cont400000+=1
  elif i==500000:
    cont500000+=1
list_sales_target=[cont100000,cont200000, cont300000, cont400000, cont500000]

plt.bar([str(i) for i in x], list_sales_target)

plt.ylabel('Frecuencia')

plt.xlabel('Objetivos de ventas')

plt.title('Usuarios de lenguajes de programación')

plt.show()

"""##Calcular el historico de ventas

Crear una función llamada historico_ventas que tomando por parámetros dos arrays de 1-D (n,) los convierta en las columnas de una matriz 2-D (n x 2). Calcule una tercera columna que contenga el resultado de multiplicar cada fila. Y devuelva la matriz [n,3].


"""

def historico_ventas(pct_ventas,sales_target):
  pct_ventas=pct_ventas.reshape((500,1))
  sales_target=sales_target.reshape((500,1))
  matriz=np.concatenate((pct_ventas,sales_target),axis=1)
  matriz=np.concatenate((matriz,np.prod(matriz,axis=1).reshape((500,1))),axis=1)
  return matriz

historico_ventas(pct_ventas,sales_target)

#@title Comprueba el histórico de ventas
def check2():
  if pct_ventas[0]*sales_target[0]==historico_ventas(pct_ventas,sales_target)[0][2] and pct_ventas[5]*sales_target[5]==historico_ventas(pct_ventas,sales_target)[5][2] and len(historico_ventas(pct_ventas,sales_target))*len(historico_ventas(pct_ventas,sales_target)[0])==1500:
    return 'Correcto'
  else:
    return 'Incorrecto'

check2()

"""#Calcular el ratio de comision para cada vendedor

Crea la funcion ratio_comision que reciba un % de ventas conseguido en tanto por uno y devuelva la comisión correspondiente según la tabla:

|% ventas conseguid|Ratio de comisión|
|---|---|
|0.8-0.9|2%|
|0.91-0.99|3%|
|>=1|4%|


"""

def ratio_comision(x):
  '''Return the commission rate based on the table:
    0-90% = 2%
    91-99% = 3%
    >= 100 = 4% '''
  if x>=0.8 and x <= .90:
      return .02
  elif x>.9 and x <= .99:
      return .03
  elif x>=1:
      return .04
  else:
    return 0

for percent in [0.7, 0.9,0.95,1]:
  print(ratio_comision(percent))

#@title Comprueba la funcion ratio_comision
def check3():
  if ratio_comision(0.99)==0.03 and ratio_comision(0.6)==0 and ratio_comision(1.5)==0.04:
    return 'Correcto'
  else:
    return 'Incorrecto'
check3()

"""##Calcular ratio de comision y cantidad de comision para los 500 empleados

Crea la función comision, que tomando una matriz (donde la primera columna es el porcentaje de objetivo de ventas conseguido, la segunda es el objetivo de ventas y la tercera, las ventas conseguidas) devuelva la matriz introducida como parámetro con dos columnas más (la cuarta será el ratio de comisión y la quinta la comision que hay que pagar a dicho empleado).


"""

def comision(matriz):
  list_ratio_comision=np.array([ratio_comision(i) for i in matriz[:,0]])
  matriz=np.concatenate((matriz,list_ratio_comision.reshape(500,1)),axis=1)
  comision_value=np.prod((matriz[:,2:]),axis=1)
  matriz=np.concatenate((matriz,comision_value.reshape(500,1)),axis=1)
  return matriz

comision(historico_ventas(pct_ventas,sales_target))

#@title Comprueba la función comision
def check4():
  if len(comision(historico_ventas(pct_ventas,sales_target)))==500 and len(comision(historico_ventas(pct_ventas,sales_target))[0])==5 and comision(historico_ventas(pct_ventas,sales_target))[0,2]*comision(historico_ventas(pct_ventas,sales_target))[0,3]==comision(historico_ventas(pct_ventas,sales_target))[0,4]:
    return 'Correcto'
  else:
    return 'Incorrecto'

check4()

"""##Simulacion de montecarlo

Una vez preparadas todas las herramientas necesarias vamos a crear la funcion montecarlo que tenga como parámetro el número de simulaciones que queremos hacer.

La función montecarlo deberá:

* Crear unos objetivos de ventas siguiendo la distribuccion uniforme con diferentes probabilidades.
* Crear un porcentaje de ventas alcanzado siguiendo una distribucion normal

* Calcular las ventas reales, el ratio de comisión, la comision de cada empleado.
* Guardar para cada simulación los totales de la empresa (suma de todos los empleados) de ventas, objetivo de ventas y comisiones.

* Una vez echas todas las simulaciones obtener la media, la derivación estandar, el mínimo y el máximo para cada uno de los totales de la empresa. La función debe devolver la matriz 4 x 3 con la primera columna las ventas reales, la segunda columna el objetivo de ventas y la tercera la comisión total. Y las filas: la media, la derivación estandar, el mínimo y el máximo. (En ese orden).


Entrada:

      print(montecarlo (1000))

Salida:

      [[87634053.00 87626400.00 2965409.90]
      [2566056.38 2531273.01 99840.39]
      [80266000.00 79800000.00 2667370.00]
      [96279000.00 95800000.00 3291020.00]]


"""

# creamos función montecarlo
def montecarlo(simulaciones):
  # creamos lista vacía con sus estadísticas
  all_stats=[]
  # iteramos para realizar simulaciones
  for i in range(simulaciones):
    # similamos datos con distribución de probabilidad
    sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)
    # simulamos datos con distribución normal dando una media, varianza
    pct_ventas = np.random.normal(avg, std_dev, num_reps).round(2)
    # calculamos la matriz comisión
    result_vendedor_simu=comision(historico_ventas(pct_ventas,sales_target))
    # devolvemos los resultados
    result_simu=[np.sum(result_vendedor_simu[:,2],axis=0),np.sum(result_vendedor_simu[:,1],axis=0), np.sum(result_vendedor_simu[:,-1],axis=0)]
    # añadimos los 3 resultados de cada simulación en una lista
    all_stats.append(result_simu)

  all_stats=np.array(all_stats)
  print(all_stats)
  # calculamos y devolvemos arrays con media, desviación, minimo y maximo
  return np.concatenate((np.mean(all_stats, axis=0).reshape(1,3), np.std(all_stats, axis=0).reshape(1,3), np.min(all_stats, axis=0).reshape(1,3), np.max(all_stats, axis=0).reshape(1,3)),axis=0)

print(montecarlo(1000))

#@title Comprueba la función montecarlo
montecarlo1=montecarlo(1000)
def check5():
  if montecarlo1[0,0]>=montecarlo1[2,0] and montecarlo1[0,0]<=montecarlo1[3,0]:
    return 'Correcto'
  else:
    return 'Incorrecto'
check5()

#@title Consigue el Token para corregir en Nodd3r:

import hashlib
token_result=montecarlo(1000)
pwd = hashlib.sha256(str(len(token_result)+pct_ventas.std().round(1)+pct_ventas.mean().round(1)+ len(pct_ventas)).encode())
print('El token es:\n',pwd.hexdigest())

# Ejemplo simple Monte Carlo

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
media_ventas = 1000  # Media de ventas históricas
desviacion_ventas = 100  # Desviación estándar de las ventas
num_meses = 12  # Número de meses para la simulación
num_simulaciones = 1000  # Número de simulaciones

# Simulaciones de Monte Carlo
simulaciones = np.random.normal(loc=media_ventas, scale=desviacion_ventas, size=(num_simulaciones, num_meses))

# Calcular las ventas totales para cada simulación
ventas_totales = simulaciones.sum(axis=1)

# Visualizar los resultados
plt.hist(ventas_totales, bins=50, edgecolor='black')
plt.title('Distribución de Ventas Totales en 12 Meses (Simulación Monte Carlo)')
plt.xlabel('Ventas Totales')
plt.ylabel('Frecuencia')
plt.show()

# Estadísticas de los resultados
print(f"Ventas Totales Promedio: {np.mean(ventas_totales):.2f}")
print(f"Ventas Totales Mínimas: {np.min(ventas_totales):.2f}")
print(f"Ventas Totales Máximas: {np.max(ventas_totales):.2f}")
print(f"Percentil 5% de Ventas Totales: {np.percentile(ventas_totales, 5):.2f}")
print(f"Percentil 95% de Ventas Totales: {np.percentile(ventas_totales, 95):.2f}")
