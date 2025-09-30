# Ejercicio 1: Análisis de Producción de Energía Solar - Guía Explicativa

## 📋 Contexto del Ejercicio

El **Ejercicio 1** se centra en el análisis de datos de una startup que instala paneles solares en tres barrios (A, B y C) durante 6 meses. Este ejercicio integra conceptos fundamentales de manipulación de datos con NumPy y pandas, estadística descriptiva y visualización, aplicados a un caso práctico del sector energético.

## 🎯 Objetivos de Aprendizaje

- **Manipulación de arrays multidimensionales** con NumPy
- **Construcción y manipulación de DataFrames** con pandas
- **Cálculos estadísticos** básicos (promedios, desvío estándar)
- **Visualización de datos** con matplotlib
- **Análisis económico** de participaciones y clasificaciones

## 📊 Estructura de Datos y Metodología

### A. Simulación y Armado del DataFrame

#### Conceptos Técnicos Clave

**Arrays NumPy 6×3**: La estructura fundamental del ejercicio son dos matrices de 6 filas (meses) por 3 columnas (barrios):

- `energia`: Energía producida en MWh
- `costo_unitario`: Costo por MWh

```python
# Ejemplo de estructura de datos
energia = np.array([
    [45.2, 52.8, 38.5],  # Mes 1: Barrio A, B, C
    [48.7, 55.3, 42.1],  # Mes 2
    # ... más meses
])
```

#### Construcción del DataFrame

El **DataFrame** es la herramienta central para organizar datos estructurados. La construcción sigue estos pasos:

1. **Creación del vector temporal**: `meses = np.arange(1, 7)`
2. **Estructuración de columnas**: Energía por barrio + costos unitarios
3. **Cálculo de costos totales**: `costo_total = energia × costo_unitario`
4. **Agregación de totales**: Suma mensual y totales por barrio

#### Consideraciones Económicas

- **Costos unitarios como tasas**: Se promedian (no se suman) porque representan $/MWh
- **Interpretación de totales**: Los totales mensuales muestran la evolución temporal del negocio
- **Análisis por barrio**: Identifica eficiencias relativas entre ubicaciones

### B. Análisis de Participaciones con Operaciones Vectorizadas

#### Metodología de Cálculo

**Operaciones vectorizadas** permiten realizar cálculos eficientes sobre arrays completos:

```python
# Participación porcentual
participacion_A = (costo_acumulado_A / costo_total_general) * 100
```

#### Función de Clasificación

La función `clasificar_barrio()` implementa **lógica de negocio**:

- **"clave"**: Participación ≥ 35% (barrios estratégicos)
- **"secundario"**: Participación < 35% (barrios menores)

Esta clasificación es fundamental para la **toma de decisiones** en la asignación de recursos.

### C. Estadísticas Descriptivas

#### Promedio y Variabilidad

- **Promedio**: `array.mean()` calcula la tendencia central
- **Desvío estándar**: `array.std()` mide la variabilidad de producción

#### Interpretación Económica

El **desvío estándar** es clave para evaluar la **confiabilidad** de cada ubicación:

- **Alto desvío**: Producción irregular, mayor riesgo
- **Bajo desvío**: Producción estable, menor riesgo

### D. Visualización de Datos

#### Gráfico de Líneas (Evolución Temporal)

```python
plt.plot(meses, energia_A, marker='o', label='Barrio A', linewidth=2)
```

**Propósito**: Mostrar tendencias y patrones estacionales en la producción energética.

#### Gráfico de Barras (Participaciones)

```python
plt.bar(barrios, participaciones, color=['skyblue', 'lightgreen', 'lightcoral'])
```

**Propósito**: Comparar la importancia relativa de cada barrio en el negocio.

## 🔍 Análisis Económico Profundo

### Conceptos de Gestión Energética

1. **Diversificación geográfica**: Los tres barrios representan una estrategia de diversificación de riesgo
2. **Economías de escala**: Los barrios con mayor producción pueden tener ventajas de costo
3. **Análisis de eficiencia**: La relación producción/costo identifica ubicaciones óptimas

### Indicadores Clave de Performance (KPIs)

- **Producción total por barrio**: Mide el tamaño del mercado
- **Costo promedio por MWh**: Evalúa la eficiencia operativa
- **Variabilidad de producción**: Cuantifica el riesgo operativo
- **Participación en costos**: Identifica la concentración del negocio

## 💻 Implementación en Python

### Herramientas y Librerías

```python
import numpy as np           # Operaciones matemáticas y arrays
import pandas as pd          # Manipulación de datos estructurados
import matplotlib.pyplot as plt  # Visualización de datos
```

### Patrones de Código Importantes

1. **Indexación de arrays**: `energia[:, 0]` selecciona toda la primera columna
2. **Concatenación de DataFrames**: `pd.concat()` para agregar filas de totales
3. **Operaciones elemento a elemento**: `array1 * array2` para cálculos vectorizados
4. **Formateo de salida**: `f"{valor:,.2f}"` para presentación profesional

### Buenas Prácticas

- **Comentarios descriptivos**: Explicar el propósito económico de cada cálculo
- **Validación de resultados**: Verificar que los totales sean consistentes
- **Visualización clara**: Usar colores y etiquetas que faciliten la interpretación
- **Variables con nombres semánticos**: `costo_acumulado_A` es más claro que `var1`

## 🎓 Conexión con el Currículo FCE-UBA

Este ejercicio integra conceptos de:

- **Estadística Económica**: Medidas de tendencia central y dispersión
- **Análisis de Inversiones**: Evaluación de proyectos por ubicación
- **Gestión de Operaciones**: Optimización de recursos y eficiencia
- **Economía de la Energía**: Análisis sectorial y sostenibilidad

### Referencias a Material de Cátedra

- **Sesión 2**: `2_Manipulación_de_datos_organizacionales_y_visualización.ipynb` - Fundamentos de manipulación de datos
- **Sesión 1**: `1_Introducción_a_python_para_el_manejo_de_datos_organizacional.ipynb` - Conceptos básicos de arrays y DataFrames

## 📈 Aplicaciones Prácticas

### En el Mundo Real

1. **Empresas de energía renovable**: Evaluación de sitios para parques solares/eólicos
2. **Fondos de inversión**: Análisis de portafolios de activos energéticos
3. **Gobiernos locales**: Planificación de políticas energéticas regionales
4. **Consultoras**: Estudios de factibilidad para proyectos sustentables

### Extensiones Posibles

- **Análisis estacional**: Incorporar factores climáticos
- **Proyecciones**: Modelos predictivos basados en tendencias históricas
- **Optimización**: Algoritmos para asignación óptima de recursos
- **Análisis de sensibilidad**: Evaluación de escenarios alternativos

## 🔚 Conclusiones

El Ejercicio 1 establece las bases fundamentales para el análisis de datos en contextos económicos. La combinación de herramientas técnicas (NumPy, pandas, matplotlib) con conceptos de gestión empresarial prepara a los estudiantes para enfrentar problemas reales del sector energético y de la economía en general.

La metodología desarrollada - desde la simulación de datos hasta la interpretación de resultados - es aplicable a múltiples sectores y constituye una competencia central para profesionales de ciencias económicas en la era de los datos.
