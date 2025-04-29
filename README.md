# Simulación Monte Carlo para Comisiones de Ventas

Este proyecto realiza una **simulación de Monte Carlo** para modelar el cálculo de **comisiones de vendedores** según distintos escenarios de desempeño. La simulación estima valores esperados de ventas reales, objetivos alcanzados y comisiones pagadas con base en la distribución de probabilidad de diferentes variables.

---

## 🧮 Descripción del modelo

El script simula 1,000 escenarios de ventas, en cada uno de los cuales se generan 500 vendedores con:

- Un **porcentaje de logro de ventas** (distribución normal).
- Un **objetivo de ventas asignado** (distribución discreta con pesos).
- Una **comisión asignada** basada en escalas de rendimiento.

---

## ⚙️ Lógica de cálculo

1. **Generación de porcentajes de venta:**  
   Basado en una distribución normal (media 1, desviación típica 0.1).

2. **Asignación de objetivos:**  
   Valores posibles: 100k, 200k, 300k, 400k, 500k con probabilidades [60%, 20%, 10%, 5%, 5%].

3. **Cálculo de ventas reales:**  
   `ventas_reales = porcentaje_logro × objetivo`

4. **Escalas de comisión:**

   | Porcentaje logrado | Comisión |
   |--------------------|----------|
   | 80% - 90%          | 2%       |
   | 91% - 99%          | 3%       |
   | 100% o más         | 4%       |
   | Menos del 80%      | 0%       |

5. **Salida de la simulación:**  
   Se presentan media, desviación típica, mínimo y máximo de:
   - Ventas reales totales
   - Objetivos totales
   - Comisiones totales

---

## 📊 Visualizaciones

Se incluyen histogramas para:

- La distribución de porcentaje de ventas alcanzadas.
- La distribución de objetivos asignados.

---

## ▶️ Cómo ejecutar

Asegúrate de tener Python 3 y las librerías necesarias:

```bash
pip install numpy matplotlib
````

Luego ejecuta el script:

````bash
python simulacion_montecarlo.py
````

## 📁 Estructura

````bash
Copiar
Editar
simulacion_montecarlo.py    # Código principal
README.md                   # Este archivo
````
## 🧠 Ideas de mejora futura

Agregar interfaz gráfica o web.

Permitir personalización de escalas de comisión y probabilidades.

Exportar resultados a Excel o CSV.

Añadir pruebas unitarias y validación de inputs.

## 📃 Licencia

Este proyecto es libre para uso educativo y profesional. Puedes modificarlo y reutilizarlo con atribución.
