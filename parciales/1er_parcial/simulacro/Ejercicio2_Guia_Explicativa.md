# Ejercicio 2: Modelo de Insumo-Producto Suizo - Guía Explicativa Completa

## 📋 Contexto del Ejercicio

El **Ejercicio 2** aborda el análisis macroeconómico de la economía suiza mediante el **modelo de insumo-producto de Leontief**. Este ejercicio integra tres sectores emblemáticos: chocolates (C), relojes (R) y servicios financieros (SF), analizando las interdependencias sectoriales y el impacto de shocks externos (tarifas estadounidenses).

## 🎯 Objetivos de Aprendizaje

- **Comprensión del modelo de Leontief**: Fundamentos teóricos y aplicación práctica
- **Análisis de interdependencias sectoriales**: Cómo los sectores se relacionan entre sí
- **Cálculo de efectos multiplicadores**: Propagación de impactos económicos
- **Interpretación de valor agregado**: Concepto fundamental del PIB
- **Análisis de política económica**: Evaluación de impactos de tarifas comerciales

## 🏗️ Fundamentos Teóricos del Modelo Insumo-Producto

### ¿Qué es una Matriz Sectorial?

La **matriz sectorial** (también llamada matriz de transacciones intermedias) registra los flujos de bienes y servicios entre sectores de la economía. En nuestro caso:

```text
| SECTORES | C | R | SF |
|----------|---|---|----| 
| C        | 90| 20| 80 |
| R        |200|500|400 |
| SF       |180|280|1000|
```

**Interpretación clave**:

- **Filas**: Sectores que **venden** (proveedores)
- **Columnas**: Sectores que **compran** (demandantes)
- **Elemento (i,j)**: Cantidad que el sector j compra del sector i

### El Concepto de Interdependencia Sectorial

**Pregunta fundamental**: *¿Cómo puede un sector comprar y vender a otro sector?*

**Respuesta**: Los sectores representan **agregaciones de empresas** que requieren insumos para producir:

1. **Sector Chocolates → Sector Relojes**: Las empresas relojeras suizas compran chocolates para regalos VIP
2. **Sector Relojes → Sector Chocolates**: Las chocolateras compran maquinaria de precisión (tecnología relojera)
3. **Sector Servicios Financieros → Ambos**: Provee servicios bancarios, seguros y financiamiento

### El Vector de Valor Agregado: Más que un Ajuste Contable

El **valor agregado** NO es simplemente una variable de ajuste para "hacer cuadrar las cuentas". Representa la **riqueza nueva** creada por cada sector:

**Fórmula**: `V.A._j = X_j - Σ(insumos intermedios que compra el sector j)`

**Componentes del valor agregado**:

- **Sueldos y salarios**: Remuneración al trabajo
- **Ganancias empresariales**: Retorno al capital
- **Impuestos**: Ingresos del gobierno
- **Depreciación**: Desgaste del capital físico

**Importancia macroeconómica**: `PIB = Σ(Valor Agregado de todos los sectores)`

## 📊 Procedimiento de Resolución Paso a Paso

### a) Construcción del DataFrame y Cálculo del Producto Total

#### Conceptos Fundamentales

**Dos métodos de cálculo equivalentes**:

1. **Por filas** (enfoque de ventas):
   ```python
   X_i = Σ(matriz_sectorial[i,:]) + H_i
   ```
   *"El producto total es lo que vendo a otros sectores más lo que vendo al consumo final"*

2. **Por columnas** (enfoque de compras):
   ```python
   X_j = Σ(matriz_sectorial[:,j]) + V.A._j
   ```
   *"El producto total es lo que compro de insumos más el valor que agrego"*

#### Implementación en Python

```python
# Método por filas (ventas)
producto_total = matriz_sectorial.sum(axis=1) + demanda_final

# Verificación por columnas (compras + valor agregado)
verificacion_X = matriz_sectorial.sum(axis=0) + valor_agregado
```

### b) Matriz de Coeficientes Técnicos

#### Concepto Económico

Los **coeficientes técnicos** `a_ij` representan la **intensidad tecnológica** de uso de insumos:

**Fórmula**: `a_ij = Z_ij / X_j`

**Interpretación**: Cantidad de insumo del sector i necesaria para producir **1 unidad monetaria** del sector j.

#### Análisis de Estructura Productiva

```python
# Cálculo de la matriz A
coeficientes_tecnicos = matriz_sectorial / producto_total.reshape(1, -1)
```

**Interpretación de resultados**:
- **Suma alta por columna**: Sector intensivo en insumos intermedios (más interdependiente)
- **Suma baja por columna**: Sector intensivo en valor agregado (más autónomo)

### c) Impacto de Shocks Externos: Las Tarifas Estadounidenses

#### Modelado del Shock

Las tarifas representan un **shock de demanda externa**:
- Chocolates: -5%
- Relojes: -40%  
- Servicios Financieros: -90%

```python
demanda_final_nueva = demanda_final_original * np.array([0.95, 0.60, 0.10])
```

#### Lógica Económica

Este tipo de shock simula:
- **Proteccionismo comercial**: EE.UU. protege industrias domésticas
- **Guerra comercial**: Escalada de tensiones económicas
- **Cambios geopolíticos**: Reconfiguración de cadenas de valor globales

### d) El Modelo de Leontief: Cálculo de Efectos Multiplicadores

#### Fundamento Matemático

**Ecuación de Leontief**: `X = (I - A)^(-1) × H`

**Donde**:
- `X`: Vector de producto total
- `I`: Matriz identidad
- `A`: Matriz de coeficientes técnicos  
- `H`: Vector de demanda final

#### Interpretación de la Matriz Inversa

La matriz `(I - A)^(-1)` contiene los **multiplicadores de Leontief**:
- **Elemento (i,j)**: Cuánto debe aumentar la producción del sector i cuando la demanda final del sector j aumenta en 1 unidad
- **Diagonal**: Efectos directos
- **Fuera de la diagonal**: Efectos indirectos (interdependencias)

#### Implementación

```python
matriz_identidad = np.eye(3)
matriz_I_menos_A = matriz_identidad - coeficientes_tecnicos
matriz_leontief = np.linalg.inv(matriz_I_menos_A)
producto_total_nuevo = matriz_leontief @ demanda_final_nueva
```

### e) Cálculo del Nuevo Valor Agregado

#### Metodología

Una vez conocido el nuevo producto total, el valor agregado se recalcula manteniendo la **estructura tecnológica**:

```python
# Los coeficientes técnicos se mantienen constantes
insumos_intermedios_nuevos = coeficientes_tecnicos.T @ producto_total_nuevo
valor_agregado_nuevo = producto_total_nuevo - insumos_intermedios_nuevos
```

## 🔍 Análisis Económico Profundo

### Efectos Multiplicadores: Más Allá del Impacto Directo

**Resultado clave**: Una reducción de 1,049 millones CHF en demanda final genera una caída de 2,584 millones CHF en producto total.

**Multiplicador**: 2.46

**Interpretación**: Por cada franco suizo de reducción en demanda externa, la economía suiza pierde 2.46 francos en producción total debido a las interdependencias sectoriales.

### Cambio en el Liderazgo Económico

**Antes**: Servicios Financieros dominaba (2,460 millones CHF)
**Después**: Relojes se convierte en líder (716 millones CHF)

**Implicaciones**:
1. **Reestructuración sectorial**: La economía se vuelve menos financiera
2. **Vulnerabilidad**: Dependencia excesiva del sector externo más afectado
3. **Resiliencia relativa**: El sector relojero muestra mayor estabilidad

### Impacto en el PIB Nacional

**Caída del PIB**: 56.5% (de 1,880 a 817 millones CHF)

Esta magnitud indica una **recesión severa**, comparable a crisis económicas históricas.

## 💻 Implementación Técnica en Python

### Librerías Especializadas

```python
import numpy as np           # Álgebra lineal y operaciones matriciales
import pandas as pd          # Estructuración de datos sectoriales
import matplotlib.pyplot as plt  # Visualización de impactos
```

### Patrones de Código Avanzados

1. **Operaciones matriciales**: `@` para multiplicación de matrices
2. **Inversión de matrices**: `np.linalg.inv()` para calcular multiplicadores
3. **Reshape para broadcasting**: `.reshape(1, -1)` para divisiones elemento-columna
4. **Verificación numérica**: `np.allclose()` para validar consistencia

### Manejo de Dimensiones

```python
# Broadcasting correcto para cálculo de coeficientes
coeficientes_tecnicos = matriz_sectorial / producto_total.reshape(1, -1)
#                                           ^^^^^^^^^^^^^^^^
#                                           Convierte a fila para división por columnas
```

## 🎓 Conexión con Material de Cátedra

### Referencias Específicas

- **Sesión 5**: `5_Matrices_y_Leontief.ipynb` - Fundamentos del modelo de Leontief
- **Sesión 6**: `6_Manipulación_de_datos_estructurados_y_Leontief.ipynb` - Aplicaciones prácticas

### Conceptos Curriculares Integrados

- **Macroeconomía**: Medición del PIB por el método del valor agregado
- **Economía Internacional**: Impactos de políticas comerciales
- **Estadística Económica**: Matrices de insumo-producto nacional
- **Análisis Cuantitativo**: Álgebra matricial aplicada a la economía

## 🌍 Aplicaciones en el Mundo Real

### Usos Institucionales

1. **Bancos Centrales**: Evaluación de políticas monetarias y sus efectos sectoriales
2. **Ministerios de Economía**: Análisis de impacto de reformas estructurales  
3. **Organismos Internacionales**: Estudios de integración económica (OCDE, FMI)
4. **Consultoras**: Evaluación de inversiones y proyectos de infraestructura

### Casos de Estudio Relevantes

- **Brexit**: Impacto en cadenas de valor europeas
- **Guerra comercial EE.UU.-China**: Efectos en economías intermedias
- **Pandemia COVID-19**: Disrupciones sectoriales y recuperación
- **Transición energética**: Reconfiguración de matrices productivas

## 🔧 Extensiones y Profundizaciones

### Refinamientos Técnicos

1. **Matrices dinámicas**: Incorporar cambio tecnológico en el tiempo
2. **Modelos regionales**: Análisis subnacional con matrices estado-región
3. **Incorporación ambiental**: Matrices de insumo-producto verdes
4. **Análisis estocástico**: Modelado de incertidumbre en coeficientes

### Desarrollos Teóricos

- **Modelos de equilibrio general**: Integración con precios y mercados de factores
- **Análisis input-output social**: Incorporación de variables demográficas
- **Optimización sectorial**: Asignación óptima de recursos escasos

## 🎯 Conclusiones y Aprendizajes Clave

### Conceptos Fundamentales Dominados

1. **Interdependencia económica**: Los sectores no operan en aislamiento
2. **Efectos multiplicadores**: Los impactos se propagan por toda la economía
3. **Valor agregado como creación de riqueza**: No es solo un ajuste contable
4. **Política económica cuantitativa**: Herramientas para evaluación ex-ante

### Competencias Técnicas Desarrolladas

- **Manipulación de matrices económicas** con NumPy
- **Cálculo de multiplicadores de Leontief**
- **Análisis de sensibilidad** a shocks externos
- **Visualización de impactos macroeconómicos**

### Preparación Profesional

Este ejercicio prepara para roles en:
- **Análisis macroeconómico** en bancos centrales
- **Consultoría económica** especializada
- **Investigación aplicada** en think tanks
- **Política pública** basada en evidencia

El dominio del modelo de Leontief constituye una competencia distintiva para economistas en la era de la economía basada en datos y el análisis cuantitativo avanzado.
