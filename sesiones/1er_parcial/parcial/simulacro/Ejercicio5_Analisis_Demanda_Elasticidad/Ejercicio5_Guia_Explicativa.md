# 📱 Ejercicio 5: Guía Explicativa - Análisis de Demanda y Elasticidad

## 🎯 **Objetivo Pedagógico**

Este ejercicio integra conceptos fundamentales de **análisis de funciones**, **optimización** y **elasticidad económica** aplicados al mercado de teléfonos celulares, desarrollando competencias para:

- Calcular derivadas de orden superior y determinar la máxima derivada no nula
- Identificar y clasificar puntos críticos (máximos/mínimos locales)
- Calcular e interpretar elasticidad precio de la demanda
- Distinguir entre elasticidad continua y discreta
- Aplicar análisis matemático a decisiones empresariales reales

---

## 🧠 **Conceptos Teóricos Fundamentales**

### **1. Función de Demanda Cuadrática**

La función `Qd(p) = 180 - p² - 3p` representa una **demanda no lineal** con características especiales:

**Componentes:**
- **Término constante (180)**: Demanda máxima teórica cuando p = 0
- **Término lineal (-3p)**: Efecto proporcional del precio
- **Término cuadrático (-p²)**: Efecto acelerado del precio

**Implicaciones económicas:**
- **Función cóncava**: La demanda disminuye de forma acelerada con el precio
- **Máximo interior**: Existe un precio que maximiza la cantidad demandada
- **Realismo**: Captura mejor el comportamiento real del consumidor

### **2. Derivadas de Orden Superior**

**Primera derivada**: `dQd/dp = -2p - 3`
- **Interpretación**: Tasa de cambio marginal de la demanda
- **Signo negativo**: Confirma la ley de demanda (relación inversa)

**Segunda derivada**: `d²Qd/dp² = -2`
- **Interpretación**: Aceleración del cambio en la demanda
- **Constante negativa**: La función es uniformemente cóncava

**Derivadas superiores**: Todas son cero (función polinómica de grado 2)

### **3. Elasticidad Precio de la Demanda**

**Fórmula**: `ε = (dQd/dp) × (p/Qd)`

**Interpretación económica:**
- Mide la **sensibilidad** de la cantidad demandada ante cambios en el precio
- Expresada como **porcentaje de cambio en cantidad por porcentaje de cambio en precio**
- **Valor negativo**: Normal en bienes ordinarios (ley de demanda)

**Clasificación:**
- `|ε| > 1`: Demanda **elástica** (sensible al precio)
- `|ε| < 1`: Demanda **inelástica** (poco sensible al precio)
- `|ε| = 1`: Elasticidad **unitaria** (proporcionalidad exacta)

---

## 🛠️ **Desarrollo Paso a Paso (Enfoque Estudiantil)**

### **Parte 1: ¿Por qué buscamos la derivada de mayor orden?**

**🎯 Objetivo**: Entender completamente el comportamiento de la función.

#### **Proceso sistemático:**

1. **Primera derivada**: `dQd/dp = -2p - 3`
   - **Significado**: Cuánto cambia la demanda por cada peso de aumento en precio
   - **Siempre negativa**: Confirma que es una función de demanda válida

2. **Segunda derivada**: `d²Qd/dp² = -2`
   - **Significado**: Cómo cambia la tasa de cambio de la demanda
   - **Constante negativa**: La demanda cae de forma acelerada

3. **Tercera derivada**: `d³Qd/dp³ = 0`
   - **Significado**: No hay cambios en la aceleración
   - **Resultado**: La derivada de mayor orden no nula es la **segunda**

#### **¿Por qué importa esto?**

- Nos dice que la función es **cuadrática** (grado 2)
- Garantiza que tiene **comportamiento predecible**
- Confirma que tendrá **un solo máximo o mínimo**

### **Parte 2: ¿Cómo encontramos y clasificamos puntos críticos?**

#### **Paso 1: Encontrar puntos críticos**

```python
# Igualamos la primera derivada a cero
-2p - 3 = 0
p = -3/2 = -1.5
```

**🚫 Problema**: p = -1.5 es **negativo** (precio negativo no tiene sentido económico)

#### **Paso 2: Buscar el máximo en el dominio válido**

Como la función es cóncava (segunda derivada negativa) y no tiene puntos críticos en el dominio positivo, el máximo se encuentra **en el borde del dominio**.

**Análisis del dominio económico:**
- **p ≥ 0**: Los precios no pueden ser negativos
- **Qd ≥ 0**: La demanda no puede ser negativa

**Encontrar dónde Qd = 0:**
```python
180 - p² - 3p = 0
p² + 3p - 180 = 0
```

Usando la fórmula cuadrática: p = 12 (tomamos la raíz positiva)

**Conclusión**: El dominio válido es **0 ≤ p ≤ 12**

#### **Paso 3: Identificar el máximo real**

Evaluando en el punto crítico teórico (p = -1.5):
- `Qd(-1.5) = 180 - (-1.5)² - 3(-1.5) = 180 - 2.25 + 4.5 = 182.25`

**Interpretación**: El máximo teórico está fuera del dominio económico, pero nos da información sobre la forma de la función.

### **Parte 3: ¿Cómo calculamos e interpretamos la elasticidad?**

#### **Fórmula aplicada:**

```python
ε(p) = (dQd/dp) × (p/Qd)
ε(p) = (-2p - 3) × (p/(180 - p² - 3p))
```

#### **Evaluación en puntos específicos:**

**Para p = $1k:**
- `Qd(1) = 180 - 1 - 3 = 176k teléfonos`
- `ε(1) = (-2-3) × (1/176) = -5/176 ≈ -0.028`
- **Interpretación**: Demanda **muy inelástica** (|ε| << 1)

**Para p = $5k:**
- `Qd(5) = 180 - 25 - 15 = 140k teléfonos`
- `ε(5) = (-10-3) × (5/140) = -13/28 ≈ -0.464`
- **Interpretación**: Demanda **inelástica** (|ε| < 1)

**Para p = $10k:**
- `Qd(10) = 180 - 100 - 30 = 50k teléfonos`
- `ε(10) = (-20-3) × (10/50) = -23/5 = -4.6`
- **Interpretación**: Demanda **muy elástica** (|ε| >> 1)

#### **Patrón observado:**

- **Precios bajos**: Demanda inelástica (los consumidores no son muy sensibles)
- **Precios altos**: Demanda elástica (los consumidores son muy sensibles)
- **Transición gradual**: La elasticidad cambia suavemente a lo largo de la curva

### **Parte 4: ¿Qué diferencia hay entre elasticidad continua y discreta?**

#### **Elasticidad Continua (lo que calculamos):**

**Características:**
- Usa **derivadas** (cambios infinitesimales)
- Mide elasticidad en **un punto específico**
- **Matemáticamente exacta**
- Ideal para **análisis teórico**

**Fórmula**: `ε = (dQ/dp) × (p/Q)`

#### **Elasticidad Discreta (elasticidad de arco):**

**Características:**
- Usa **diferencias finitas** (cambios observables)
- Mide elasticidad **entre dos puntos**
- **Práctica para datos reales**
- Ideal para **análisis empresarial**

**Fórmula**: `ε = (ΔQ/ΔP) × (P_promedio/Q_promedio)`

#### **Ejemplo comparativo (p = $3k a p = $7k):**

```python
# Elasticidad Discreta
P₁ = 3, Q₁ = 162
P₂ = 7, Q₂ = 110
ε_discreta = (110-162)/(7-3) × (5/136) ≈ -0.479

# Elasticidad Continua (en p = 5)
ε_continua = (-13) × (5/140) ≈ -0.464

# Diferencia: 3.2%
```

---

## 📊 **Elementos Visuales del Ejercicio**

### **1. Curva de Demanda**

- **Forma parabólica**: Cóncava hacia abajo
- **Interceptos**: (0, 180) en eje Y, (12, 0) en eje X
- **Máximo teórico**: Fuera del dominio económico
- **Interpretación**: Demanda típica con efectos no lineales

### **2. Gráfico de Elasticidad**

- **Función hiperbólica**: ε(p) cambia drásticamente
- **Zona inelástica**: Precios bajos (|ε| < 1)
- **Zona elástica**: Precios altos (|ε| > 1)
- **Punto de elasticidad unitaria**: Donde |ε| = 1

### **3. Comparación Elasticidad Continua vs Discreta**

- **Secante vs Tangente**: Visualización de las diferencias metodológicas
- **Puntos de evaluación**: Marcados claramente en la curva
- **Diferencias numéricas**: Cuantificadas y explicadas

---

## 🎯 **Resultados Esperados**

### **Parte 1 - Derivadas:**

- **Primera derivada**: `dQd/dp = -2p - 3`
- **Segunda derivada**: `d²Qd/dp² = -2`
- **Derivada de mayor orden**: Segunda (función cuadrática)
- **Interpretación**: Función cóncava con comportamiento predecible

### **Parte 2 - Optimización:**

- **Punto crítico teórico**: p = -1.5 (fuera del dominio)
- **Clasificación**: Máximo (segunda derivada negativa)
- **Dominio económico**: 0 ≤ p ≤ 12
- **Interpretación**: Función cóncava en todo el dominio válido

### **Parte 3 - Elasticidades:**

- **p = $1k**: ε ≈ -0.028 (muy inelástica)
- **p = $5k**: ε ≈ -0.464 (inelástica)
- **p = $10k**: ε ≈ -4.6 (muy elástica)
- **Patrón**: Elasticidad creciente con el precio

### **Parte 4 - Tipo de Elasticidad:**

- **Es elasticidad continua** (no discreta)
- **Diferencias metodológicas**: Derivadas vs diferencias finitas
- **Aplicaciones**: Teórica vs práctica
- **Ejemplo numérico**: Diferencia del 3.2% entre métodos

---

## 🔧 **Herramientas Técnicas**

### **Python - Librerías Principales:**

- `sympy`: Cálculo simbólico de derivadas y resolución de ecuaciones
- `numpy`: Evaluación numérica y generación de arrays
- `matplotlib`: Visualización de funciones y elasticidades
- `scipy.optimize`: Métodos de optimización numérica

### **Métodos Matemáticos:**

- **Cálculo diferencial**: Derivadas de orden superior
- **Análisis de funciones**: Clasificación de puntos críticos
- **Elasticidad económica**: Interpretación de sensibilidades
- **Análisis numérico**: Comparación de métodos continuo vs discreto

---

## 💡 **Conceptos Clave (Nivel Estudiantil)**

### **1. ¿Qué es una derivada de orden superior?**

*En palabras simples*: Si la primera derivada te dice qué tan rápido cambia algo, la segunda derivada te dice qué tan rápido cambia esa velocidad de cambio.

### **2. ¿Por qué una función cuadrática tiene máximo?**

*Analogía práctica*: Como lanzar una pelota hacia arriba - sube, llega a un punto máximo, y después baja. La demanda funciona igual con los precios.

### **3. ¿Qué significa elasticidad?**

*Explicación sencilla*: Si subo el precio 10% y las ventas bajan 20%, la elasticidad es -2. Significa que los clientes son muy sensibles al precio.

### **4. ¿Cuándo usar elasticidad continua vs discreta?**

- **Continua**: Para entender la teoría y hacer modelos matemáticos
- **Discreta**: Para analizar datos reales de ventas y tomar decisiones

### **5. ¿Por qué la elasticidad cambia según el precio?**

*Intuición económica*: A precios bajos, un aumento no duele tanto. A precios altos, cualquier aumento más puede ser la gota que colma el vaso.

---

## 🌍 **Aplicaciones en el Mundo Real**

### **En Estrategia de Precios:**

- **Identificación de precios óptimos**: Dónde maximizar ingresos vs volumen
- **Análisis de sensibilidad**: Qué tan arriesgado es subir precios
- **Segmentación de mercado**: Diferentes elasticidades por grupo de consumidores

### **En Planificación de Marketing:**

- **Campañas promocionales**: Cuándo los descuentos son más efectivos
- **Lanzamiento de productos**: Estrategia de precios de penetración vs descremado
- **Análisis competitivo**: Comparar elasticidades con la competencia

### **En Análisis Financiero:**

- **Forecasting de ingresos**: Predecir ventas ante cambios de precio
- **Análisis de escenarios**: Evaluación de riesgos de políticas de precios
- **Optimización de portafolio**: Balancear productos por elasticidad

---

## ✅ **Criterios de Evaluación**

**Lo que el profesor va a revisar:**

### **Competencias Matemáticas:**

- Cálculo correcto de derivadas de orden superior
- Identificación de la derivada de mayor orden no nula
- Clasificación correcta de puntos críticos usando segunda derivada
- Aplicación precisa de la fórmula de elasticidad

### **Interpretación Económica:**

- Explicación del significado de cada derivada en contexto económico
- Justificación de por qué la función tiene máximo o mínimo
- Clasificación correcta de elasticidades (elástica/inelástica)
- Interpretación práctica de los valores de elasticidad

### **Análisis Crítico:**

- Distinción clara entre elasticidad continua y discreta
- Explicación de cuándo usar cada método
- Evaluación de las diferencias entre ambos enfoques
- Conexión entre resultados matemáticos y decisiones empresariales

### **Presentación de Resultados:**

- Código Python funcional y bien documentado
- Visualizaciones claras con interpretaciones apropiadas
- Desarrollo lógico de cada parte del problema
- Síntesis final integrando todos los conceptos aplicados