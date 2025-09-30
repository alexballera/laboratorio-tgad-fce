# Guías de Estilo de Código Estudiantil - FCE-UBA

## Objetivo
Estas instrucciones garantizan que el código generado por IA mantenga un estilo auténtico de estudiante de FCE-UBA, evitando la detección como contenido generado por inteligencia artificial.

## 📋 INSTRUCCIÓN CRÍTICA INICIAL
**SIEMPRE PREGUNTAR AL INICIO:** ¿Esta actividad es para:
- **🎓 ESTUDIO/PRÁCTICA** (código detallado con explicaciones pedagógicas)
- **📝 ENTREGA/EVALUACIÓN** (código estilo estudiante real)

---

## 🎯 Diferencias por Contexto

### 🎓 MODO ESTUDIO/PRÁCTICA
- ✅ Comentarios detallados y pedagógicos
- ✅ Explicaciones conceptuales extensas
- ✅ Múltiples métodos alternativos
- ✅ Docstrings completas
- ✅ Verificaciones y validaciones extra

### 📝 MODO ENTREGA/EVALUACIÓN
- ⚠️ **APLICAR LAS SIGUIENTES REGLAS ESTRICTAMENTE**

---

## 🔒 REGLAS PARA CÓDIGO "ESTILO ESTUDIANTE" (Entrega/Evaluación)

### 1. **Comentarios Reducidos y Naturales**
```python
# ❌ EVITAR (demasiado profesional):
# i. Array de energía producida (en MWh) - 6 meses × 3 barrios
# Simulamos datos realistas de producción de energía solar

# ✅ USAR (estilo estudiante):
# Arrays de energia y costos
```

### 2. **Sin Docstrings en Funciones Simples**
```python
# ❌ EVITAR:
def clasificar_barrio(participacion):
    """
    Clasifica un barrio según su participación en el costo total.
    Parámetros: ...
    """

# ✅ USAR:
def clasificar_barrio(participacion):
    # Funcion para clasificar barrios
```

### 3. **Sin Explicaciones Técnicas Profundas**
```python
# ❌ EVITAR:
# EXPLICACIÓN: pd.concat() une dos DataFrames verticalmente
# pd.DataFrame([totales_por_barrio]) convierte el diccionario...

# ✅ USAR:
# Agregamos la fila de totales
```

### 4. **Sin Métodos Alternativos Comentados**
```python
# ❌ EVITAR:
# MÉTODO ALTERNATIVO (más directo para agregar una fila):
# df_final = df_energia_costos.copy()

# ✅ USAR: Solo un método, el más directo
```

### 5. **Sin Verificaciones Múltiples**
```python
# ❌ EVITAR:
# Verificación alternativa usando el DataFrame (debe dar el mismo resultado)
print(f"Barrio A: {datos_meses['A'].mean():.2f} MWh")

# ✅ USAR: Solo el cálculo principal
```

### 6. **Nombres de Variables Simples**
```python
# ❌ EVITAR:
datos_meses = df_final.iloc[:-1]
costo_acumulado_A = datos_meses['costo_total_A'].sum()

# ✅ USAR:
df_datos = df_final.iloc[:-1]
total_A = df_datos['costo_total_A'].sum()
```

### 7. **Menos Formateo Perfecto**
```python
# ❌ EVITAR:
print("\n" + "="*50)
print("DATAFRAME FINAL CON TOTALES POR BARRIO:")
print("="*50)

# ✅ USAR:
print("Dataframe final:")
```

### 8. **Sin Emojis ni Símbolos Decorativos**
```python
# ❌ EVITAR (típico de IA):
# ✅ Calculamos los totales
# 🔍 Analizamos los resultados

# ✅ USAR (estilo estudiante):
# Calculamos los totales
# Analizamos los resultados
```

### 9. **Errores Menores Típicos de Estudiantes**
- Variables en español mezcladas con inglés
- Espaciado inconsistente ocasional
- Comentarios más informales
- Menos uso de f-strings (usar .format() a veces)

### 10. **Estructura Más Simple**
```python
# ❌ EVITAR (demasiado estructurado):
# Paso 1: Calculamos...
# Paso 2: Agregamos...

# ✅ USAR (más directo):
# Calculamos costos totales
# Agregamos totales
```

### 11. **Prints Más Básicos**
```python
# ❌ EVITAR:
print(f"   Barrio A: ${costo_acumulado_A:,.2f}")

# ✅ USAR:
print("Barrio A:", round(costo_acumulado_A, 2))
```

---

## 📊 Comparación Estilo Real FCE-UBA

### Estilo Original del Curso:
```python
#Importamos las librerías que vamos a utilizar
import numpy as np #para hacer operaciones matemáticas

# Armamos una matriz que contenga datos de producción
matriz_produccion = np.array([
    [150, 200, 100],  # Planta Norte
    [180, 150, 120]   # Planta Centro
])
print(matriz_produccion)
```

### Aplicar Este Estilo:
- Comentarios simples y directos
- Sin exceso de explicaciones
- Formateo básico pero correcto
- Variables descriptivas pero no excesivamente largas

---

## ⚖️ Nivel de Complejidad Apropiado

### ✅ INCLUIR (Nivel FCE-UBA):
- Operaciones básicas de numpy y pandas
- Gráficos simples con matplotlib
- Estadísticas descriptivas básicas
- Funciones simples con if/else

### ❌ EVITAR (Demasiado Avanzado):
- Métodos avanzados de pandas
- Optimizaciones complejas
- Programación orientada a objetos
- Librerías especializadas no vistas en clase

---

## 🎯 Checklist Final para Entrega/Evaluación

Antes de entregar código, verificar:

- [ ] ¿Los comentarios son simples y directos?
- [ ] ¿No hay docstrings en funciones básicas?
- [ ] ¿No hay explicaciones técnicas profundas?
- [ ] ¿No hay métodos alternativos comentados?
- [ ] ¿Las variables tienen nombres simples pero descriptivos?
- [ ] ¿El formateo es básico pero correcto?
- [ ] ¿La complejidad es apropiada para el nivel del curso?
- [ ] ¿Parece escrito por un estudiante de economía aprendiendo Python?

---

## 📝 Nota Final
Estos lineamientos son para **garantizar autenticidad académica** cuando el código será evaluado. Para sesiones de estudio, mantener el estilo pedagógico detallado que facilita el aprendizaje.