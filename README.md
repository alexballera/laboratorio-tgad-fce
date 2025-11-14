# 📊 Laboratorio TGAD (FCE - UBA)

> **Tecnicatura de Gestión y Análisis de Datos**  
> Facultad de Ciencias Económicas - Universidad de Buenos Aires

Repositorio académico con materiales, prácticas y recursos para el curso de análisis de datos aplicado a ciencias económicas.

---

## 📖 Descripción

Este repositorio contiene todo el material necesario para la **Tecnicatura de Gestión y Análisis de Datos (TGAD)** de la FCE-UBA. El enfoque está en la **aplicación práctica** de Python para:

- 📈 Manipulación y análisis de datos económicos
- 📊 Visualización de información empresarial
- 🧮 Modelización de funciones económicas
- 💹 Análisis de inversiones y finanzas
- 🔬 Optimización y programación lineal
- 📉 Cálculo diferencial e integral aplicado

---

## 🚀 Guía de Inicio Rápido

### Requisitos Previos

- **Python 3.10+** instalado
- **Git** para clonar el repositorio
- Editor de código (recomendado: **VS Code** o **Jupyter Lab**)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/alexballera/laboratorio-tgad-fce.git
cd laboratorio-tgad-fce
```

### Paso 2: Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Linux/Mac:
source .venv/bin/activate

# En Windows:
.venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Iniciar Jupyter Lab

```bash
jupyter lab
```

¡Listo! Ya puedes empezar a trabajar con los notebooks del curso.

---

## 📁 Estructura del Proyecto

```text
laboratorio-tgad-fce/
│
├── 📂 sesiones/                # Contenido organizado por parciales
│   ├── 1er_parcial/           # Sesiones 1-12 + Parcial 1
│   │   ├── sesion1_Introducción_a_python/
│   │   ├── sesion2_Manipulación_de_datos/
│   │   ├── sesion3_Modelización_de_funciones/
│   │   ├── sesion4_Puntos_de_equilibrio/
│   │   ├── sesion5_Matrices_y_Leontief/
│   │   ├── sesion6_Manipulación_estructurada/
│   │   ├── sesion7_Programación_lineal/
│   │   ├── sesion9_Derivada_y_elasticidades/
│   │   ├── sesion11_Optimización_de_funciones/
│   │   ├── sesion12_Duopolio/
│   │   └── parcial/           # Material del primer parcial
│   │
│   └── 2do_parcial/           # Sesiones 13-17
│       ├── sesion13_Integrales_Indefinidas1/
│       ├── sesion14_Aplicación_Integrales/
│       ├── sesion15_Integrales_Definidas/
│       ├── sesion16_Análisis_inversiones/
│       └── sesion17_Aplicaciones_inversiones/
│
├── 📂 actividades/            # Actividades prácticas semanales
│   ├── actividad1/           # Introducción a NumPy y Pandas
│   ├── actividad2/           # Manipulación de datos
│   ├── actividad3/           # Visualización
│   ├── actividad4/           # Análisis exploratorio
│   ├── actividad9/           # Derivadas y variaciones
│   ├── actividad13/          # Integrales
│   └── actividad16/          # Inversiones
│
├── 📂 resumenes/             # Trabajos integradores
│   ├── integracion1-graficos-dataframe--recap-inversiones/
│   ├── integradora1_1_integrales/
│   └── integradora2_2_finanzas/
│
├── 📂 utils/                 # Utilidades y funciones reutilizables
│   ├── matematicas_financieras.py    # Biblioteca de funciones financieras
│   └── test_matematicas_financieras.py
│
├── 📂 fuentes/              # Material de referencia y datasets
│
├── 📄 requirements.txt      # Dependencias del proyecto
├── 📄 AGENTS.md            # Instrucciones para asistentes de IA
├── 📄 README_SETUP.md      # Guía de configuración detallada
└── 📄 LICENSE              # Licencia MIT

```

---

## 🛠️ Tecnologías y Librerías

### Core de Análisis de Datos

- **NumPy** 2.3.2 - Computación numérica
- **Pandas** 2.3.2 - Manipulación de datos
- **Matplotlib** 3.10.5 - Visualización estática
- **Seaborn** 0.13.2 - Visualización estadística

### Análisis Científico y Estadístico

- **SciPy** 1.16.1 - Computación científica
- **Scikit-learn** 1.7.1 - Machine Learning
- **Statsmodels** 0.14.5 - Modelos estadísticos

### Finanzas y Optimización

- **numpy-financial** 1.0.0 - Cálculos financieros
- **yfinance** 0.2.40 - Datos financieros en tiempo real
- **PuLP** 2.8.0 - Programación lineal
- **mplfinance** 0.12.10b0 - Gráficos financieros

### Visualización Avanzada

- **Plotly** 6.3.0 - Gráficos interactivos
- **Panel** 1.5.4 - Dashboards
- **WordCloud** 1.9.3 - Nubes de palabras

### Entorno de Desarrollo

- **Jupyter Lab** 4.4.6 - Ambiente de notebooks
- **IPyKernel** 6.30.1 - Kernel de Python
- **IPyWidgets** 8.1.7 - Widgets interactivos

---

## 📚 Contenido del Curso

### 🎯 Primer Parcial (Sesiones 1-12)

| Sesión | Tema | Conceptos Clave |
|--------|------|-----------------|
| **1** | Introducción a Python | NumPy, arrays, operaciones básicas |
| **2** | Manipulación de datos | Pandas, DataFrames, limpieza de datos |
| **3** | Modelización de funciones | Funciones económicas, oferta y demanda |
| **4** | Puntos de equilibrio | Sistemas de ecuaciones, break-even |
| **5** | Matrices y Leontief | Álgebra matricial, modelo input-output |
| **6** | Datos estructurados | Joins, merge, groupby avanzado |
| **7** | Programación lineal | Optimización con PuLP, problemas de asignación |
| **9** | Derivadas y elasticidades | Cálculo diferencial, análisis marginal |
| **11** | Optimización | Máximos y mínimos, funciones de varias variables |
| **12** | Duopolio | Teoría de juegos, equilibrio de Nash |

### 🎯 Segundo Parcial (Sesiones 13-17)

| Sesión | Tema | Conceptos Clave |
|--------|------|-----------------|
| **13** | Integrales Indefinidas | Primitivas, técnicas de integración |
| **14** | Aplicación de Integrales | Costos totales, funciones acumuladas |
| **15** | Integrales Definidas | Áreas bajo la curva, excedentes |
| **16** | Análisis de inversiones I | VAN, TIR, flujos de caja |
| **17** | Análisis de inversiones II | Evaluación de proyectos, numpy-financial |

---

## 🔧 Utilidades Disponibles

### Módulo `utils/matematicas_financieras.py`

Biblioteca completa de funciones financieras documentadas:

```python
from utils.matematicas_financieras import (
    present_value,      # Valor presente (PV)
    future_value,       # Valor futuro (FV)
    net_present_value,  # Valor actual neto (VAN/NPV)
    internal_rate_return, # Tasa interna de retorno (TIR/IRR)
    payback_period,     # Período de recuperación
    # ... y muchas más
)
```

**Incluye:**

- ✅ Funciones de valor temporal del dinero
- ✅ Cálculo de anualidades
- ✅ Análisis de bonos
- ✅ Evaluación de proyectos de inversión
- ✅ Conversión de tasas de interés
- ✅ Tests unitarios incluidos

### Script `utils/check_uncommitted_changes.py`

Verificador de cambios sin commitear para operaciones seguras en la nube:

```bash
# Verificación básica
python utils/check_uncommitted_changes.py

# Modo estricto (incluye archivos no rastreados)
python utils/check_uncommitted_changes.py --strict
```

**Características:**

- ✅ Detecta archivos modificados sin commitear
- ✅ Detecta cambios en staging sin commit
- ✅ Modo estricto para archivos no rastreados
- ✅ Integrado con GitHub Actions
- ✅ Mensajes descriptivos en español
- ✅ Tests unitarios incluidos

Ver documentación completa en [`utils/README.md`](./utils/README.md)

---

## 📝 Flujo de Trabajo Recomendado

### Para Cada Sesión

1. **Revisar materiales** en la carpeta `sesiones/`
2. **Seguir los notebooks** con ejemplos paso a paso
3. **Completar actividades** en la carpeta `actividades/`
4. **Consultar `utils/`** para funciones reutilizables
5. **Revisar resúmenes** integradores antes de evaluaciones

### Convenciones de Código

```python
# Bloque de importación estándar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización
plt.figure(figsize=(8, 5))
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
```

---

## 🤝 Para Estudiantes

### ¿Cómo usar este repositorio?

1. **Clonar y configurar** siguiendo la Guía de Inicio Rápido
2. **Navegar por sesiones** según el cronograma del curso
3. **Practicar con actividades** para reforzar conceptos
4. **Consultar resúmenes** como material de repaso
5. **Usar funciones de `utils/`** en tus propios análisis

### Consejos

- 💡 Los comentarios están en **español** para facilitar el aprendizaje
- 📖 Cada notebook incluye **objetivos de aprendizaje** claros
- 🎓 Los ejemplos tienen **contexto económico y empresarial real**
- 🔍 Usa los tests en `utils/` como referencia de buenas prácticas

---

## 📖 Documentación Adicional

- **[AGENTS.md](./AGENTS.md)** - Instrucciones completas para asistentes de IA y estándares del proyecto
- **[README_SETUP.md](./README_SETUP.md)** - Guía detallada de configuración del entorno
- **[LICENSE](./LICENSE)** - Licencia MIT del proyecto

---

## 🤖 Trabajo con Asistentes de IA

Este proyecto incluye instrucciones específicas para trabajar con GitHub Copilot y otros asistentes de IA. Consulta **[AGENTS.md](./AGENTS.md)** para:

- Estándares de código académico
- Convenciones de notebooks
- Guías de estilo para estudiantes
- Flujos de trabajo didácticos

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver archivo [LICENSE](./LICENSE) para más detalles.

---

## 👥 Autor

**Alex Ballera**  
Estudiante FCE-UBA  
📧 Contacto: [GitHub](https://github.com/alexballera)

---

## 🌟 Contribuciones

Este es un repositorio académico personal. Si tienes sugerencias o mejoras:

1. Abre un **Issue** para discutir cambios
2. Haz un **Fork** del repositorio
3. Envía un **Pull Request** con tus mejoras

---

**¡Éxitos en tu aprendizaje de análisis de datos aplicado a economía!** 📊🎓
