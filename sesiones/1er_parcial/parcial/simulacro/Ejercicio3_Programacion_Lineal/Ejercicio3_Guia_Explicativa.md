# Ejercicio 3 - Guía Explicativa: Programación Lineal para Estudiantes FCE-UBA

## 📋 Resumen Ejecutivo

**Tema Central**: Optimización de la producción en Techint usando herramientas de Python
**Conceptos Clave**: Maximizar beneficios, minimizar costos, limitaciones empresariales, análisis de escenarios
**Herramientas**: `scipy.optimize.linprog` (nivel básico), gráficos explicativos, interpretación económica

---

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Plantear problemas empresariales** como problemas de optimización matemática
2. **Usar Python para resolver problemas de optimización** con `scipy.optimize.linprog`
3. **Interpretar resultados numéricos** en términos de decisiones empresariales
4. **Graficar limitaciones y soluciones** para entender visualmente el problema
5. **Analizar "qué pasa si..."** cambian las condiciones del mercado
6. **Comparar diferentes objetivos empresariales** (maximizar vs minimizar)

---

## 📚 Marco Teórico

### 🔍 **¿Qué es la Programación Lineal?**

La **programación lineal** es una herramienta matemática que nos ayuda a tomar la **mejor decisión** cuando tenemos **recursos limitados**.

#### **¿Cuándo la usamos en empresas?**

- 🏭 **Decidir qué producir** cuando tenemos límites de espacio, dinero o tiempo
- 💰 **Maximizar ganancias** o **minimizar costos**
- 📦 **Optimizar el uso de recursos** como materiales, personal, presupuesto

#### **Componentes básicos (en español sencillo):**

1. **¿Qué queremos decidir?** (Variables): Cantidades a producir, comprar, vender, etc.
2. **¿Qué queremos lograr?** (Objetivo): Ganar más dinero, gastar menos, ser más eficientes
3. **¿Qué nos limita?** (Restricciones): Presupuesto, espacio, tiempo, recursos disponibles
4. **¿Qué podemos hacer realmente?** (Región factible): Todas las opciones que respetan nuestras limitaciones

#### **Estructura típica de un problema:**

```
DECIDIR: ¿Cuánto producir de cada producto?
OBJETIVO: Maximizar beneficio total = precio₁×cantidad₁ + precio₂×cantidad₂ + ...
LIMITACIONES: 
    - No gastar más del presupuesto disponible
    - No usar más espacio del que tenemos
    - Producir al menos lo mínimo requerido
    - No producir cantidades negativas
```

### 🏭 **Contexto Empresarial: Techint**

**Techint** es una empresa argentina multinacional especializada en:
- Producción de acero, cobre y hierro
- Gestión de recursos limitados (capacidad, presupuesto)
- Optimización de beneficios empresariales

---

## 🛠️ Desarrollo Paso a Paso (Enfoque Estudiantil)

### **Parte A: Plantear el Problema en Palabras**

#### **🎯 ¿Qué tenemos que decidir?**
- Cantidad de acero a producir (llamémosla A)
- Cantidad de cobre a producir (llamémosla C)  
- Cantidad de hierro a producir (llamémosla H)

#### **💰 ¿Qué queremos lograr?** 
Ganar la mayor cantidad de dinero posible:
- Cada tonelada de acero nos da $5 millones
- Cada tonelada de cobre nos da $10 millones
- Cada tonelada de hierro nos da $9 millones

**En fórmula:** Beneficio Total = 5×A + 10×C + 9×H

#### **⚠️ ¿Qué nos limita?**

1. **Espacio de almacenamiento:** Solo podemos guardar 1200 toneladas en total
   - A + C + H ≤ 1200

2. **Dinero disponible:** Solo tenemos $1500 millones para producir
   - Acero cuesta $2 millones/ton → 2×A
   - Cobre cuesta $3 millones/ton → 3×C  
   - Hierro cuesta $4 millones/ton → 4×H
   - Total: 2×A + 3×C + 4×H ≤ 1500

3. **Lógica básica:** No podemos producir cantidades negativas
   - A ≥ 0, C ≥ 0, H ≥ 0

### **Parte B: Resolver con Python**

#### **🔧 Configuración del Problema:**

```python
import numpy as np
from scipy.optimize import linprog

# Lo que queremos maximizar (beneficios)
beneficios = [5, 10, 9]  # Acero, Cobre, Hierro

# TRUCO: Python minimiza por defecto, pero queremos maximizar
# Solución: convertir a negativo
c = [-5, -10, -9]  # Ahora minimizar esto = maximizar beneficios

# Las limitaciones como matrices
limitaciones = [
    [1, 1, 1],    # Capacidad: A + C + H ≤ 1200
    [2, 3, 4]     # Presupuesto: 2A + 3C + 4H ≤ 1500
]
maximos = [1200, 1500]

# Resolver
resultado = linprog(c, A_ub=limitaciones, b_ub=maximos, 
                   bounds=[(0,None), (0,None), (0,None)])
```

#### **📊 Interpretación de Resultados:**

- **¿La solución es válida?** → `resultado.success == True`
- **¿Cuánto producir?** → `resultado.x` (cantidades óptimas)
- **¿Cuánto ganamos?** → `-resultado.fun` (beneficio máximo)

### **Parte C: Entender Visualmente**

#### **🎨 ¿Por qué hacer gráficos?**

Los gráficos nos ayudan a **ver** las limitaciones y entender por qué esa es la mejor solución.

**Concepto clave:** La zona azul en el gráfico = "todas las combinaciones posibles"
- **Dentro de la zona:** ✅ Factible (podemos hacerlo)
- **Fuera de la zona:** ❌ Imposible (viola alguna limitación)
- **Esquinas de la zona:** 🎯 Candidatos a solución óptima

### **Parte D: Análisis "¿Qué Pasa Si...?"**

#### **🌍 Escenario Real: Sube el Dólar**

**Situación:** El tipo de cambio se dispara, los costos aumentan:
- Acero: de $2 a $3.8 millones/ton (+90%)
- Cobre: de $3 a $4.8 millones/ton (+60%)
- Hierro: de $4 a $6 millones/ton (+50%)

**Pregunta clave:** ¿Cómo cambia nuestra estrategia de producción?

**Método:** Resolver el mismo problema pero con nuevos costos

**Interpretación económica:**
- Si un producto se vuelve muy caro de hacer, probablemente produzcamos menos
- El beneficio total va a ser menor
- Puede cambiar completamente qué productos conviene fabricar más

### **Parte E: Cambio de Objetivo Empresarial**

#### **🔄 Nuevo Problema: Supervivencia**

**Situación:** El dueño dice "No quiero ganar mucho, solo sobrevivir gastando lo mínimo"

**Nuevas reglas:**
- **Objetivo:** Minimizar gastos (no maximizar ganancias)
- **Capacidad:** Solo 800 toneladas (menos espacio)
- **Mínimos:** Para mantener la empresa:
  - Al menos 4 ton de acero
  - Al menos 2 ton de cobre
  - Al menos 8 ton de hierro

**Cambio técnico:** Ahora usamos `c = [3.8, 4.8, 6]` (costos positivos para minimizar)

---

## 🎨 Elementos Visuales del Ejercicio

### **1. Gráficos de Barras Comparativos**

- **Antes vs Después**: Cambios en niveles de producción
- **Por Producto**: Comparación individual de cada material
- **Interpretación**: Fácil comprensión de impactos

### **2. Gráficos de Torta**

- **Distribución porcentual**: Composición del mix de productos  
- **Antes/Después**: Cambios en la estrategia de producción
- **Interpretación**: Proporción relativa de cada material

### **3. Visualización de Regiones Factibles**

- **Espacios 2D**: Proyección de problemas 3D
- **Líneas de restricción**: Límites visuales claros
- **Punto óptimo**: Marcado claramente en el gráfico

---

## � Resultados Esperados

### **Problema Original (Maximización de Beneficio):**

- **Solución esperada**: Producción alta del producto más rentable (cobre)
- **Uso de recursos**: Aprovechamiento máximo de capacidades disponibles
- **Beneficio**: Valor monetario óptimo alcanzable

### **Con Aumento de Costos:**

- **Reducción general**: Menor capacidad de producción total
- **Cambio de estrategia**: Posible modificación del mix de productos
- **Impacto económico**: Cuantificación de pérdidas por inflación

### **Minimización de Presupuesto:**

- **Producción mínima**: Solo lo necesario para supervivencia
- **Eficiencia de costos**: Menor gasto posible
- **Estrategia defensiva**: Enfoque en continuidad operativa

---

## 🔧 Herramientas Técnicas Utilizadas

### **Python - Librerías Principales:**
- `scipy.optimize.linprog`: Resolución de problemas de programación lineal
- `numpy`: Operaciones matriciales y vectoriales
- `matplotlib`: Visualización de resultados y regiones factibles
- `pandas`: Organización y presentación de datos

### **Métodos de Optimización:**
- **Algoritmo Simplex**: Método estándar para programación lineal
- **Método de puntos interiores**: Alternativa eficiente para problemas grandes
- **Análisis gráfico**: Verificación visual de soluciones

---

## 💡 Conceptos Clave para Recordar

### **1. Teorema Fundamental de la Programación Lineal:**
La solución óptima (si existe) siempre se encuentra en un vértice de la región factible.

### **2. Análisis de Sensibilidad:**
Pequeños cambios en parámetros pueden llevar a grandes cambios en la solución óptima.

### **3. Dualidad:**
Todo problema de maximización tiene un problema dual de minimización asociado.

### **4. Restricciones Activas:**
Las restricciones que se cumplen con igualdad en la solución óptima determinan la solución.

### **5. Interpretación Económica:**
- **Variables de holgura**: Recursos no utilizados completamente
- **Precios sombra**: Valor marginal de relajar una restricción
- **Análisis de factibilidad**: Verificación de existencia de soluciones

---

## 🚀 Aplicaciones Empresariales

### **En Gestión de Operaciones:**
- **Planificación de producción**: Determinar qué y cuánto producir
- **Asignación de recursos**: Optimizar uso de capacidad y presupuesto
- **Mix de productos**: Balancear portafolio según rentabilidad

### **En Finanzas Corporativas:**
- **Presupuesto de capital**: Seleccionar proyectos de inversión
- **Gestión de riesgo**: Diversificar exposición manteniendo retorno
- **Planificación estratégica**: Escenarios de crecimiento óptimo

### **En Supply Chain:**
- **Localización de plantas**: Minimizar costos de transporte y producción
- **Gestión de inventarios**: Balancear costos de mantener vs stockout
- **Redes de distribución**: Optimizar flujos de productos

---

## 📝 Preguntas de Reflexión

1. **¿Qué sucede si una restricción se vuelve redundante?**
2. **¿Cómo interpretarías una solución con variables de holgura positivas?**
3. **¿Qué indica cuando la solución óptima está en el origen (0,0,0)?**
4. **¿Por qué los problemas de programación lineal siempre tienen soluciones en vértices?**
5. **¿Cómo cambiaría el análisis si los beneficios también dependieran del tipo de cambio?**

---

## 🎯 Puntos Clave para Examen

### **Formalización Matemática:**
- Identificar variables de decisión correctamente
- Escribir función objetivo con coeficientes apropiados
- Formular restricciones según limitaciones del problema

### **Interpretación de Resultados:**
- Explicar el significado económico de la solución óptima
- Identificar restricciones activas y su implicación
- Analizar cambios ante variaciones en parámetros

### **Visualización y Análisis:**
- Interpretar gráficos de regiones factibles
- Identificar puntos óptimos visualmente
- Comparar escenarios mediante gráficos

### **Pensamiento Crítico:**
- Evaluar factibilidad de soluciones
- Proponer mejoras o alternativas
- Relacionar resultados con decisiones empresariales reales

---

*Esta guía proporciona una base sólida para comprender y aplicar programación lineal en contextos de gestión empresarial, con énfasis en la interpretación económica y la toma de decisiones basada en optimización matemática.*