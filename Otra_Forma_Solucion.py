# simulacion_montecarlo.py
# -*- coding: utf-8 -*-
"""
. Estructura organizada en funciones claras.

. Comentarios y documentación para cada sección.

. Remoción de código redundante o confuso.

. Estilo PEP8 para Python.

. Preparado como script completo de Python.
"""
  
"""
Simulación de Monte Carlo para presupuestar comisiones de ventas
"""

import numpy as np
import matplotlib.pyplot as plt

# Configuración general
np.set_printoptions(formatter={'float_kind': "{:.2f}".format})
avg = 1
std_dev = 0.1
num_reps = 500
sales_target_values = [100000, 200000, 300000, 400000, 500000]
sales_target_prob = [.6, .2, .1, .05, .05]

def generar_pct_ventas(n=500, avg=1.0, std_dev=0.1):
    """Genera porcentajes de ventas alcanzados con distribución normal."""
    return np.random.normal(avg, std_dev, n).round(2)

def generar_objetivos_ventas(n=500):
    """Genera objetivos de ventas simulados basados en probabilidades."""
    return np.random.choice(sales_target_values, n, p=sales_target_prob)

def historico_ventas(pct_ventas, sales_target):
    """Combina porcentaje de ventas y objetivos en matriz [pct, objetivo, ventas reales]."""
    pct_ventas = pct_ventas.reshape((num_reps, 1))
    sales_target = sales_target.reshape((num_reps, 1))
    ventas_reales = (pct_ventas * sales_target).reshape((num_reps, 1))
    return np.hstack((pct_ventas, sales_target, ventas_reales))

def ratio_comision(porcentaje):
    """Asigna ratio de comisión basado en porcentaje conseguido."""
    if 0.8 <= porcentaje <= 0.90:
        return 0.02
    elif 0.91 <= porcentaje <= 0.99:
        return 0.03
    elif porcentaje >= 1.0:
        return 0.04
    else:
        return 0

def comision(matriz):
    """Añade ratio y comisión final a la matriz de ventas."""
    ratios = np.array([ratio_comision(x) for x in matriz[:, 0]]).reshape(num_reps, 1)
    comisiones = (matriz[:, 2].reshape(num_reps, 1) * ratios).reshape(num_reps, 1)
    return np.hstack((matriz, ratios, comisiones))

def montecarlo(simulaciones=1000):
    """Simula múltiples escenarios de ventas y devuelve estadísticos agregados."""
    all_stats = []

    for _ in range(simulaciones):
        pct_ventas = generar_pct_ventas(num_reps, avg, std_dev)
        sales_target = generar_objetivos_ventas(num_reps)
        matriz = comision(historico_ventas(pct_ventas, sales_target))
        total_ventas = np.sum(matriz[:, 2])
        total_objetivo = np.sum(matriz[:, 1])
        total_comision = np.sum(matriz[:, 4])
        all_stats.append([total_ventas, total_objetivo, total_comision])

    all_stats = np.array(all_stats)
    media = np.mean(all_stats, axis=0)
    std = np.std(all_stats, axis=0)
    minimo = np.min(all_stats, axis=0)
    maximo = np.max(all_stats, axis=0)

    return np.vstack([media, std, minimo, maximo])

def plot_histograma_pct_ventas(pct_ventas):
    """Grafica distribución de porcentajes de ventas alcanzados."""
    bins = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    etiquetas = ['70-80%', '80-90%', '90-100%', '100-110%', '110-120%', '>120%']
    frecs = [np.sum((pct_ventas > bins[i]) & (pct_ventas <= bins[i+1])) for i in range(len(bins)-1)]
    frecs.append(np.sum(pct_ventas > 1.2))
    
    plt.bar(etiquetas, frecs)
    plt.title("Distribución de % de ventas alcanzado")
    plt.xlabel("Rango %")
    plt.ylabel("Frecuencia")
    plt.show()

def plot_histograma_objetivos(sales_target):
    """Grafica distribución de objetivos de ventas simulados."""
    x = [str(val) for val in sales_target_values]
    frecs = [np.sum(sales_target == val) for val in sales_target_values]
    
    plt.bar(x, frecs)
    plt.title("Distribución de objetivos de ventas")
    plt.xlabel("Objetivo (€)")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    print("Ejecutando simulación Monte Carlo para comisiones de ventas...\n")
    resultados = montecarlo(1000)
    print("Resultados (media, desviación, mínimo, máximo):\n")
    print("[Ventas reales, Objetivo ventas, Comisión total (€)]")
    print(resultados)

    # Simulación para graficar distribución de inputs
    pct_ventas = generar_pct_ventas()
    sales_target = generar_objetivos_ventas()
    plot_histograma_pct_ventas(pct_ventas)
    plot_histograma_objetivos(sales_target)

if __name__ == "__main__":
    main()
