# Ejercicio 4: Análisis de Funciones de Beneficio - Guía Explicativa (Versión Simplificada)

## 📋 Contexto del Ejercicio

El **Ejercicio 4** se enfoca en el análisis de funciones de beneficio de una empresa textil, aplicando conceptos básicos de **optimización** usando Python. Este ejercicio está diseñado para estudiantes de FCE-UBA que están aprendiendo los fundamentos de análisis económico con herramientas computacionales.

## 🎯 Objetivos de Aprendizaje

- **Análisis de funciones cuadráticas** en contextos empresariales
- **Optimización básica** sin uso de derivadas complejas
- **Interpretación económica** de máximos y mínimos
- **Visualización de funciones** económicas con matplotlib
- **Toma de decisiones** basada en análisis cuantitativo

## 📊 Estructura Metodológica

### A. Función de Beneficio Cuadrática

#### Modelo Económico
La función **B(q) = -2q² + 120q - 1000** representa:

- **Término cuadrático (-2q²)**: Rendimientos decrecientes (típico en producción)
- **Término lineal (120q)**: Ingreso marginal inicial
- **Término constante (-1000)**: Costos fijos

#### Interpretación Empresarial
```python
def beneficio(q):
    return -2*q**2 + 120*q - 1000
```

**Significado económico:**
- A medida que se produce más, los beneficios inicialmente crecen
- Después de cierto punto, comienzan a decrecer (sobreproducción)
- Existe un punto óptimo que maximiza beneficios

### B. Optimización usando Fórmula del Vértice

#### Metodología Simplificada
Para funciones cuadráticas **f(x) = ax² + bx + c**, el máximo/mínimo está en:

**x = -b/(2a)**

En nuestro caso:
- a = -2, b = 120, c = -1000
- q* = -120/(2×(-2)) = 30

#### Ventajas Pedagógicas
- **Sin derivadas**: Apropiado para nivel introductorio
- **Fórmula directa**: Fácil de recordar y aplicar
- **Verificación numérica**: Se puede comprobar probando valores cercanos

### C. Análisis de Puntos de Equilibrio

#### Resolución de Ecuaciones Cuadráticas
Para encontrar cuando **B(q) = 0**:
**-2q² + 120q - 1000 = 0**

Dividiendo por -2: **q² - 60q + 500 = 0**

Usando fórmula cuadrática: **q = [60 ± √(3600-2000)]/2 = [60 ± 40]/2**

**Resultados:** q₁ = 10, q₂ = 50

#### Interpretación Económica
- **Entre 10 y 50 unidades**: La empresa tiene beneficios positivos
- **Menos de 10 unidades**: Pérdidas (costos fijos altos)
- **Más de 50 unidades**: Pérdidas (sobreproducción)

## 🔧 Herramientas Técnicas Utilizadas

### Librerías Básicas
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

**Justificación:** Solo librerías fundamentales, sin herramientas avanzadas como `sympy` o `scipy.optimize`.

### Visualización Efectiva
- **Gráficos de línea**: Para mostrar comportamiento de la función
- **Marcadores de puntos**: Para identificar valores clave
- **Anotaciones**: Para facilitar interpretación

### Análisis de Escenarios
```python
datos_resumen = {
    'Escenario': ['No producir', 'Punto equilibrio 1', 'Producción óptima', 'Punto equilibrio 2'],
    'Cantidad': [0, 10, 30, 50],
    'Beneficio': [beneficios correspondientes]
}
```

## 💡 Enfoque Pedagógico

### Nivel Apropiado para FCE-UBA
- **Matemática básica**: Álgebra y funciones cuadráticas
- **Sin cálculo diferencial**: Evita derivadas e integrales
- **Enfoque práctico**: Soluciones directas y aplicables
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