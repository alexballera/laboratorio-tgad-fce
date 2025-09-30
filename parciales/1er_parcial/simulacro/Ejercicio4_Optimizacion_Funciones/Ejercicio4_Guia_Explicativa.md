# Ejercicio 4: Función de Producción y Derivadas Parciales - Guía Explicativa

## 📋 Contexto del Ejercicio

El **Ejercicio 4** se enfoca en el análisis de **funciones de producción Cobb-Douglas** usando derivadas parciales con SymPy. Este ejercicio está diseñado para estudiantes de FCE-UBA que aprenden fundamentos de microeconomía aplicada con herramientas computacionales básicas.

## 🎯 Objetivos de Aprendizaje

- **Derivadas parciales** con SymPy (nivel básico)
- **Evaluación de funciones** en puntos específicos
- **Análisis de funciones de producción** Cobb-Douglas
- **Identificación de costos fijos vs variables**
- **Optimización simple** usando derivadas

## 📊 Estructura Metodológica

### Parte a: Función de Producción Cobb-Douglas

#### Modelo Económico
La función **q = x^(1/2) * y^(1/2)** representa:

- **Función Cobb-Douglas**: Forma estándar q = A·x^α·y^β donde α = β = 0.5
- **Rendimientos constantes a escala**: α + β = 1
- **Sustitución imperfecta**: Capital y trabajo son complementarios

#### Derivadas Parciales
```python
# Productividad marginal del capital
dq_dx = sp.diff(q, x)  # = √y/(2√x)

# Productividad marginal del trabajo  
dq_dy = sp.diff(q, y)  # = √x/(2√y)
```

**Significado económico:**
- **∂q/∂x**: Cuánto aumenta la producción por una unidad adicional de capital
- **∂q/∂y**: Cuánto aumenta la producción por una unidad adicional de trabajo

### Parte b: Evaluación en Puntos Específicos

#### Metodología de Evaluación
Para evaluar derivadas en (2,2):
```python
dq_dx_en_punto = dq_dx.subs([(x, 2), (y, 2)])
```

#### Interpretación en (2,2)
- **∂q/∂x|(2,2) = 0.5**: Una unidad más de capital aumenta producción en 0.5
- **∂q/∂y|(2,2) = 0.5**: Una unidad más de trabajo aumenta producción en 0.5
- **Simetría**: En este punto, ambos insumos tienen igual productividad marginal

### Parte c: Análisis Conceptual de Optimización

#### Función Objetivo vs Restricción
- **Función objetivo**: Maximizar q = √(x·y) (maximizar producción)
- **Restricción**: C = x + 2y + 100 = constante (limitación presupuestaria)
- **Herramienta**: Análisis básico de derivadas parciales
- **Punto óptimo**: Combinación que maximiza producción dado el presupuesto

### Parte d: Nueva Función de Costo

#### d.i: Análisis de Componentes
**Nueva función**: C = x + 2x² + 100

- **Insumo clave**: Solo capital (x), el trabajo desaparece
- **Costo fijo**: 100 (independiente de x)
- **Costo variable**: x + 2x² (lineal + cuadrático)

#### d.ii: Optimización de Eficiencia
**Función objetivo**: Maximizar eficiencia = q/C = √x/(x + 2x² + 100)

**Metodología**:
```python
d_eficiencia_dx = sp.diff(eficiencia, x)
puntos_criticos = sp.solve(d_eficiencia_dx, x)
```

## 🔧 Herramientas Técnicas Utilizadas

### Librerías Principales
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
```

**Justificación de SymPy:** Necesario para cálculos simbólicos de derivadas parciales (similar a sesión 12 del curso).

### Funciones Clave
- **sp.symbols()**: Definir variables simbólicas
- **sp.diff()**: Calcular derivadas parciales
- **sp.solve()**: Resolver ecuaciones
- **sp.subs()**: Evaluar expresiones en puntos específicos

### Visualización
- **Gráfico de eficiencia**: Muestra comportamiento de q/C vs capital
- **Punto óptimo marcado**: Identificación visual del máximo

## 💡 Enfoque Pedagógico FCE-UBA

### Nivel Apropiado 
- **Derivadas parciales básicas**: Nivel sesión 12 del curso
- **Sin Lagrange**: Evita complicaciones teóricas avanzadas
- **Enfoque práctico**: Evaluación numérica y interpretación económica
- **Estilo profesores**: Similar a notebooks de sesiones 9 y 12

### Conexión Curricular
- **Microeconomía**: Funciones de producción Cobb-Douglas
- **Matemática aplicada**: Derivadas parciales con SymPy
- **Optimización**: Conceptos básicos sin herramientas avanzadas

## 🎯 Conexión con Fuentes del Proyecto

### Alineación con Sesiones Teóricas
- **Sesión 9**: Derivadas y variaciones de funciones organizacionales
- **Sesión 12**: Optimización de funciones aplicado a la gestión
- **Metodología**: Similar a notebooks de profesores (funciones básicas, gráficos interpretativos)

## � Criterios de Evaluación

### Competencias Técnicas
1. **Cálculo de derivadas parciales** con SymPy
2. **Evaluación de funciones** en puntos específicos
3. **Interpretación económica** de resultados
4. **Identificación de componentes** de funciones de costo

### Competencias Analíticas
1. **Análisis conceptual** de optimización
2. **Distinción entre costos fijos y variables**
3. **Interpretación de eficiencia productiva**
4. **Justificación económica** de resultados óptimos
- **Interpretación económica**: Cada resultado se explica en términos empresariales

### Metodología Incremental
1. **Definición de funciones**: Paso a paso con explicaciones
2. **Visualización**: Gráficos que facilitan comprensión
3. **Optimización**: Métodos algebraicos simples
4. **Análisis**: Interpretación económica clara
5. **Toma de decisiones**: Recomendaciones prácticas

### Elementos Didácticos
- **Emojis y formato visual**: Facilita seguimiento
- **Verificaciones numéricas**: Confirma resultados teóricos
- **Ejemplos concretos**: Empresa textil (contexto familiar)
- **Tabla resumen**: Síntesis clara de resultados

## 📋 Criterios de Evaluación

### Competencias Técnicas
1. **Implementación de funciones** en Python
2. **Aplicación de fórmulas** algebraicas básicas
3. **Interpretación de gráficos** económicos
4. **Cálculo de puntos críticos** sin derivadas

### Competencias Analíticas
1. **Identificación de máximos** y mínimos
2. **Análisis de puntos de equilibrio**
3. **Interpretación económica** de resultados
4. **Formulación de recomendaciones** empresariales

### Competencias Comunicativas
1. **Presentación clara** de resultados
2. **Justificación** de decisiones
3. **Uso apropiado** de terminología económica
4. **Síntesis ejecutiva** para toma de decisiones

## 🔍 Diferencias con Versión Avanzada

### Elementos Eliminados
- **Derivadas parciales**: Demasiado avanzado para el nivel
- **Optimización con restricciones**: Requiere Lagrange
- **Librerías especializadas**: `sympy`, `scipy.optimize`
- **Funciones multivariables**: Complejidad innecesaria

### Elementos Conservados
- **Optimización básica**: Usando álgebra elemental
- **Análisis gráfico**: Fundamental para comprensión
- **Interpretación económica**: Núcleo del ejercicio
- **Toma de decisiones**: Objetivo final

## 🎯 Conexión con Fuentes del Proyecto

### Alineación con Sesiones Teóricas
- **Sesión 3**: Modelización de funciones económicas
- **Sesión 4**: Puntos de equilibrio y sistemas de ecuaciones
- **Metodología**: Similar a notebooks de profesores (funciones básicas, gráficos interpretativos)

### Nivel Apropiado
- **Sin matemática avanzada**: Coherente con curso introductorio
- **Enfoque aplicado**: Prioriza interpretación sobre formalismo matemático
- **Herramientas básicas**: Solo librerías fundamentales de Python

Este enfoque simplificado mantiene la riqueza conceptual del análisis económico mientras permanece accesible para estudiantes de FCE-UBA en su primer parcial.