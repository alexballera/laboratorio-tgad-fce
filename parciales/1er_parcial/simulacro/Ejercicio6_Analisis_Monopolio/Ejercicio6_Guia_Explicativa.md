# 🏭 Ejercicio 6: Guía Explicativa - Análisis de Monopolio

## 📋 **Descripción del Ejercicio**

El Ejercicio 6 presenta un **monopolio con funciones específicas** que debe ser analizado usando métodos cuantitativos. Los estudiantes trabajarán con:

**Demanda directa:** Q(p) = 500 - 10p - 3p²
**Costo total:** C(q) = 100 + 2q

El ejercicio requiere **convertir la demanda a forma inversa**, **optimizar beneficios** y **analizar comparativamente** los efectos de la competencia.

## 🎯 **Objetivos de Aprendizaje**

Al completar este ejercicio, los estudiantes serán capaces de:

- **Resolver ecuaciones cuadráticas** aplicadas a funciones de demanda económica
- **Aplicar técnicas de optimización** para maximización de beneficios empresariales
- **Calcular excedente del consumidor** usando integración numérica con Python
- **Analizar estructuras de mercado** comparando monopolio versus duopolio
- **Interpretar resultados económicos** en contexto de política de competencia

---

## 📖 **Estructura del Ejercicio (7 Pasos)**

### **Paso 1: Conversión de Demanda Directa a Inversa**

**¿Qué hace el estudiante?**
- Parte de Q(p) = 500 - 10p - 3p²
- Convierte a p(q) usando fórmula cuadrática
- Implementa la función `demanda_inversa(q)` en Python
- Verifica la conversión con valores de prueba

**¿Por qué es importante?**
La demanda inversa permite expresar el precio como función de la cantidad, facilitando la optimización de beneficios donde la variable de decisión es cuánto producir.

**Herramientas técnicas:**
- Algebra: resolución de ecuaciones cuadráticas
- Python: función con manejo de arrays y validación numérica
- Verificación: comprobación bidireccional de la conversión

### **Paso 2: Definición de Funciones Económicas**

**¿Qué hace el estudiante?**
- Define `costo_total(q) = 100 + 2*q`
- Crea `ingreso_total(q) = demanda_inversa(q) * q`
- Construye `beneficio(q) = ingreso_total(q) - costo_total(q)`
- Genera tabla comparativa con diferentes cantidades

**¿Por qué es importante?**
Estas funciones son los building blocks del análisis económico. El estudiante ve cómo se relacionan precio, cantidad, ingresos, costos y beneficios.

**Herramientas técnicas:**
- Programación: definición de funciones modulares
- Pandas: creación de DataFrames para análisis tabular
- Análisis económico: interpretación de las relaciones

### **Paso 3: Optimización de Beneficios**

**¿Qué hace el estudiante?**
- Usa métodos numéricos para encontrar el máximo de la función de beneficio
- Identifica q_optimo, p_optimo y beneficio_maximo
- Verifica la condición de segundo orden (d²Π/dq² < 0)
- Calcula ingreso y costo en el punto óptimo

**¿Por qué es importante?**
Es el corazón del análisis de monopolio: encontrar la cantidad y precio que maximizan beneficios aplicando la regla IMg = CMg.

**Herramientas técnicas:**
- Optimización numérica: uso de `np.linspace` y `np.argmax`
- Cálculo: aproximación de derivadas para verificación
- Análisis económico: interpretación del equilibrio

### **Paso 4: Cálculo del Excedente del Consumidor**

**¿Qué hace el estudiante?**
- Calcula el área bajo la curva de demanda hasta q_optimo
- Resta el área del rectángulo (p_optimo × q_optimo)
- Usa integración numérica con `np.trapezoid`
- Presenta resultados en tabla resumen

**¿Por qué es importante?**
El excedente del consumidor mide el bienestar de los consumidores, concepto clave para análisis de política económica.

**Herramientas técnicas:**
- Integración numérica: método del trapecio
- Pandas: presentación estructurada de resultados
- Visualización conceptual: interpretación geométrica del excedente

### **Paso 5: Visualización del Monopolio**

**¿Qué hace el estudiante?**
- Crea gráfico con curva de demanda y costo marginal
- Marca el punto óptimo del monopolio
- Muestra el área del excedente del consumidor
- Incluye anotaciones con valores clave

**¿Por qué es importante?**
La visualización integra todos los conceptos anteriores en una representación gráfica comprehensiva.

**Herramientas técnicas:**
- Matplotlib: gráficos económicos profesionales
- Manejo de arrays: filtrado y validación de datos
- Presentación: escalas apropiadas (0-400 x 0-25)

### **Paso 6: Análisis Teórico del Duopolio**

**¿Qué hace el estudiante?**
- Analiza teóricamente los efectos de tener dos empresas
- Simula un escenario de duopolio (modelo Cournot simplificado)
- Calcula nuevo excedente del consumidor
- Compara numéricamente monopolio vs duopolio

**¿Por qué es importante?**
Desarrolla pensamiento crítico sobre estructuras de mercado y sus efectos en el bienestar social.

**Herramientas técnicas:**
- Análisis comparativo: cálculo de cambios porcentuales
- Simulación económica: aproximación de equilibrio de duopolio
- Interpretación de política: efectos de la competencia

### **Paso 7: Comparación Visual Optimizada**

**¿Qué hace el estudiante?**
- Crea gráficos comparativos con escalas mejoradas (0-500 x 0-15)
- Muestra ambos escenarios en subplots coordinados
- Presenta tabla comparativa final con métricas clave
- Concluye sobre efectos de la competencia

**¿Por qué es importante?**
La comparación visual facilita la comprensión de conceptos abstractos y fortalece las conclusiones del análisis.

**Herramientas técnicas:**
- Subplots: visualización comparativa profesional
- Escalas optimizadas: mejor visibilidad de ambos puntos de equilibrio
- Tabla resumen: síntesis cuantitativa de resultados

---

## 🔧 **Aspectos Técnicos Específicos**

### **Manejo de la Función Cuadrática**

La demanda Q(p) = 500 - 10p - 3p² se reordena como:
**3p² + 10p + (q - 500) = 0**

```python
def demanda_inversa(q):
    a = 3
    b = 10
    c = q - 500
    discriminante = b**2 - 4*a*c
    # ... (código del ejercicio)
```

**Desafíos técnicos:**
- Manejo de arrays vs escalares
- Validación del discriminante (≥ 0)
- Selección de la raíz económicamente relevante
- Uso de `np.clip` para robustez numérica

### **Optimización Numérica**

En lugar de cálculo simbólico, el ejercicio usa métodos numéricos:

```python
q_detallado = np.linspace(1, 400, 1000)
beneficios_detallado = beneficio(q_detallado)
indice_max = np.argmax(beneficios_detallado)
q_optimo = q_detallado[indice_max]
```

**Ventajas del enfoque:**
- Más accesible para estudiantes sin cálculo avanzado
- Fácil verificación e interpretación
- Preparación para casos más complejos

### **Integración con `np.trapezoid`**

El cálculo del excedente usa integración numérica moderna:

```python
area_bajo_curva = np.trapezoid(p_integracion, q_integracion)
excedente_consumidor = area_bajo_curva - area_rectangulo
```

**Consideraciones técnicas:**
- Reemplazo de `np.trapz` (deprecado)
- Manejo de valores inválidos con máscaras
- Precisión apropiada para análisis económico

### **Visualización con Escalas Optimizadas**

Los gráficos comparativos usan escalas específicas:
- **Monopolio individual**: 0-400 x 0-25 (escala amplia)
- **Comparación**: 0-500 x 0-15 (escala optimizada)

**Rationale:**
- Mayor visibilidad del punto de duopolio (q≈398)
- Enfoque en rango relevante de precios
- Comparación visual más efectiva

---

## 📊 **Resultados Esperados del Ejercicio**

### **Valores Numéricos Aproximados:**

**Monopolio:**
- Cantidad óptima: q* ≈ 265 unidades
- Precio óptimo: p* ≈ 9.5 pesos
- Beneficio máximo: Π* ≈ 1,600 pesos
- Excedente consumidor: EC ≈ 430 pesos

**Duopolio (simulado):**
- Cantidad total: q ≈ 398 unidades (+50%)
- Precio: p ≈ 7.9 pesos (-17%)
- Excedente consumidor: EC ≈ 700 pesos (+63%)

### **Interpretaciones Económicas:**

**Efecto de la competencia:**
- ✅ Mayor cantidad disponible para consumidores
- ✅ Precios significativamente menores
- ✅ Sustancial aumento en bienestar del consumidor
- ❌ Beneficios empresariales divididos

**Implicaciones de política:**
- La competencia genera mayor bienestar social
- Los monopolios restringen cantidad para mantener precios altos
- La regulación antimonopolio tiene justificación económica clara

---

## 🎓 **Conexión con el Currículo FCE-UBA**

### **Para Microeconomía I:**
- **Aplicación práctica** de teoría del monopolio
- **Cuantificación** del dead-weight loss
- **Análisis comparativo** de estructuras de mercado

### **Para Métodos Cuantitativos:**
- **Integración** de álgebra, cálculo y programación
- **Optimización aplicada** a problemas empresariales
- **Interpretación** de resultados numéricos

### **Para Organización Industrial:**
- **Análisis de concentración** de mercado
- **Efectos de la competencia** en bienestar
- **Fundamentos** para política de competencia

### **Para Política Económica:**
- **Herramientas cuantitativas** para evaluación de políticas
- **Análisis de bienestar** social
- **Trade-offs** entre eficiencia y equidad

---

## ✅ **Criterios de Evaluación Específicos**

### **Competencias Técnicas (40%):**
- ✅ Conversión correcta de demanda directa a inversa
- ✅ Implementación apropiada de funciones en Python
- ✅ Optimización numérica exitosa del beneficio
- ✅ Cálculo preciso del excedente del consumidor

### **Interpretación Económica (35%):**
- ✅ Comprensión del significado económico de cada paso
- ✅ Explicación clara de la condición IMg = CMg
- ✅ Análisis apropiado de efectos de la competencia
- ✅ Conexión entre resultados matemáticos y teoría económica

### **Análisis Crítico (15%):**
- ✅ Evaluación balanceada de monopolio vs duopolio
- ✅ Consideración de limitaciones del modelo
- ✅ Reflexión sobre aplicaciones de política económica
- ✅ Propuestas de extensiones o mejoras al análisis

### **Presentación y Código (10%):**
- ✅ Código Python funcional y bien documentado
- ✅ Visualizaciones claras y profesionales
- ✅ Estructura lógica del desarrollo
- ✅ Síntesis apropiada de resultados

---

## 🌐 **Extensiones y Aplicaciones**

### **Para estudiantes avanzados:**
- Incorporar elasticidad de demanda variable
- Analizar oligopolio con n empresas
- Incluir costos fijos en el análisis
- Considerar diferenciación de productos

### **Aplicaciones empresariales:**
- Análisis de fusiones y adquisiciones
- Estrategias de entrada a mercados concentrados
- Evaluación de poder de mercado sectorial
- Diseño de políticas de precios

### **Investigación aplicada:**
- Estudios de caso en industrias argentinas
- Análisis de efectos de desregulación
- Evaluación de políticas de competencia
- Medición empírica de excedentes económicos

---

## 📚 **Material de Apoyo Recomendado**

### **Textos de referencia:**
- Pindyck & Rubinfeld: Microeconomía (Caps. 10-12)
- Tirole: The Theory of Industrial Organization (Caps. 1-2)
- Mas-Colell et al.: Microeconomic Theory (Cap. 12)

### **Recursos técnicos:**
- Documentación de NumPy/SciPy para optimización
- Matplotlib tutorials para visualización económica
- Jupyter notebooks con ejemplos similares

### **Casos de estudio:**
- Análisis de monopolios en telecomunicaciones
- Efectos de la desregulación en servicios públicos
- Políticas antimonopolio en países desarrollados