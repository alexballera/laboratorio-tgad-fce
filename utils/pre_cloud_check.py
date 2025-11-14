#!/usr/bin/env python3
"""
Wrapper para verificar el repositorio antes de operaciones en la nube.

Este script realiza múltiples verificaciones antes de permitir operaciones
en la nube como GitHub Copilot Workspace.

Uso:
    python utils/pre_cloud_check.py

Códigos de salida:
    0: Todo correcto, listo para operaciones en la nube
    1: Hay problemas que deben resolverse
"""

import sys
from check_uncommitted_changes import check_uncommitted_changes


def main():
    """Ejecuta todas las verificaciones pre-cloud."""
    print("🔍 Verificando estado del repositorio antes de operaciones en la nube...")
    print()
    
    all_checks_passed = True
    
    # Verificación 1: Cambios sin commitear
    print("📝 Verificando cambios sin commitear...")
    has_changes, message = check_uncommitted_changes(strict=False)
    print(message)
    print()
    
    if has_changes:
        all_checks_passed = False
    
    # Aquí se podrían agregar más verificaciones en el futuro:
    # - Verificar que los tests pasen
    # - Verificar que el código esté formateado
    # - Verificar que no haya TODOs críticos
    # - etc.
    
    # Resultado final
    if all_checks_passed:
        print("✅ " + "=" * 60)
        print("✅ Todas las verificaciones pasaron correctamente")
        print("✅ El repositorio está listo para operaciones en la nube")
        print("✅ " + "=" * 60)
        return 0
    else:
        print("❌ " + "=" * 60)
        print("❌ Algunas verificaciones fallaron")
        print("❌ Resuelve los problemas antes de continuar")
        print("❌ " + "=" * 60)
        return 1


if __name__ == '__main__':
    sys.exit(main())
