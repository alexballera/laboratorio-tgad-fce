# Utilidades del Proyecto

Este directorio contiene scripts y módulos reutilizables para el proyecto.

## 📋 Contenido

### 1. `matematicas_financieras.py`
Biblioteca completa de funciones financieras para cálculos de inversión, valor temporal del dinero, análisis de bonos y más.

Ver documentación completa en el módulo y tests en `test_matematicas_financieras.py`.

### 2. `check_uncommitted_changes.py`
Script para verificar cambios sin commitear en el repositorio Git antes de realizar operaciones en la nube.

#### 🎯 Propósito
Este script ayuda a prevenir la pérdida de trabajo local al detectar cambios sin commitear antes de:
- Operaciones de GitHub Copilot Workspace
- Cambio de ramas
- Operaciones en la nube
- Colaboración en equipo

#### 📖 Uso

##### Verificación rápida (recomendada)
```bash
python utils/pre_cloud_check.py
```

Este comando ejecuta todas las verificaciones necesarias antes de operaciones en la nube.

##### Uso básico (sin archivos no rastreados)
```bash
python utils/check_uncommitted_changes.py
```

Este modo verifica:
- ✅ Archivos modificados sin agregar al staging
- ✅ Archivos en staging sin commitear
- ❌ NO verifica archivos no rastreados (nuevos archivos sin `git add`)

##### Modo estricto (incluye archivos no rastreados)
```bash
python utils/check_uncommitted_changes.py --strict
```

Este modo verifica todo lo anterior MÁS:
- ✅ Archivos no rastreados (nuevos archivos sin agregar)

#### 📤 Códigos de Salida
- `0`: No hay cambios sin commitear (repositorio limpio)
- `1`: Hay cambios sin commitear
- `2`: Error al ejecutar git

#### 💡 Ejemplo de Salida

**Repositorio limpio:**
```
✅ No hay cambios sin commitear
```

**Con cambios detectados:**
```
❌ Cambios sin commitear detectados:
⚠️  2 archivo(s) modificado(s) sin agregar:
   - sesiones/sesion1/practica.ipynb
   - README.md

💡 Sugerencias:
   1. Commitea los cambios: git add . && git commit -m 'mensaje'
   2. Descarta los cambios: git restore .
   3. Guarda temporalmente: git stash
```

#### 🔗 Integración con GitHub Actions

Este script se ejecuta automáticamente en el workflow `.github/workflows/check-uncommitted.yml` que verifica el estado del repositorio en cada push o pull request.

#### 🧪 Tests

Los tests están en `test_check_uncommitted_changes.py`. Para ejecutarlos:

```bash
python -m unittest utils/test_check_uncommitted_changes.py -v
```

#### 🔧 Uso Programático

También puedes usar las funciones desde Python:

```python
from utils.check_uncommitted_changes import check_uncommitted_changes

# Verificar cambios
has_changes, message = check_uncommitted_changes(strict=False)

if has_changes:
    print(f"⚠️ Advertencia: {message}")
else:
    print("✅ Repositorio limpio")
```

---

## 📝 Convenciones

- Todos los scripts deben incluir tests
- La documentación debe estar en español
- Usar type hints en Python
- Seguir PEP 8 para el estilo de código
