#!/usr/bin/env python3
"""
Utilidad para verificar cambios no comprometidos en Git.

Este script verifica si hay cambios sin commitear en el repositorio
antes de realizar operaciones en la nube (como GitHub Copilot Workspace).

Uso:
    python check_uncommitted_changes.py [--strict]

Opciones:
    --strict    Modo estricto: también verifica archivos no rastreados

Códigos de salida:
    0: No hay cambios sin commitear
    1: Hay cambios sin commitear
    2: Error al ejecutar git
"""

import subprocess
import sys
from typing import Tuple, List


def run_git_command(command: List[str]) -> Tuple[int, str, str]:
    """
    Ejecuta un comando de git y retorna el resultado.
    
    Args:
        command: Lista con el comando y argumentos a ejecutar
        
    Returns:
        Tupla con (código_retorno, stdout, stderr)
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 2, "", str(e)


def check_uncommitted_changes(strict: bool = False) -> Tuple[bool, str]:
    """
    Verifica si hay cambios sin commitear en el repositorio.
    
    Args:
        strict: Si es True, también verifica archivos no rastreados
        
    Returns:
        Tupla con (tiene_cambios, mensaje_detalle)
    """
    # Verificar si estamos en un repositorio git
    returncode, _, stderr = run_git_command(['git', 'rev-parse', '--git-dir'])
    if returncode != 0:
        return True, "❌ Error: No se encuentra un repositorio Git en el directorio actual"
    
    # Verificar estado del repositorio
    returncode, stdout, stderr = run_git_command(['git', 'status', '--porcelain'])
    if returncode != 0:
        return True, f"❌ Error al ejecutar 'git status': {stderr}"
    
    # Analizar salida
    lines = stdout.splitlines() if stdout else []
    
    if not lines:
        return False, "✅ No hay cambios sin commitear"
    
    # Clasificar cambios
    modified_files = []
    untracked_files = []
    staged_files = []
    
    for line in lines:
        if not line:
            continue
        
        status = line[:2]
        filename = line[3:].strip()
        
        # Archivos no rastreados
        if status == '??':
            untracked_files.append(filename)
        # Archivos en staging (primera columna tiene cambio)
        elif status[0] in ['M', 'A', 'D', 'R', 'C']:
            staged_files.append(filename)
        # Archivos modificados sin agregar (segunda columna tiene cambio)
        elif status[1] in ['M', 'D']:
            modified_files.append(filename)
    
    # Construir mensaje detallado
    messages = []
    has_uncommitted = False
    
    if staged_files:
        has_uncommitted = True
        messages.append(f"⚠️  {len(staged_files)} archivo(s) en staging sin commitear:")
        for f in staged_files[:5]:  # Mostrar máximo 5 archivos
            messages.append(f"   - {f}")
        if len(staged_files) > 5:
            messages.append(f"   ... y {len(staged_files) - 5} más")
    
    if modified_files:
        has_uncommitted = True
        messages.append(f"⚠️  {len(modified_files)} archivo(s) modificado(s) sin agregar:")
        for f in modified_files[:5]:
            messages.append(f"   - {f}")
        if len(modified_files) > 5:
            messages.append(f"   ... y {len(modified_files) - 5} más")
    
    if untracked_files and strict:
        has_uncommitted = True
        messages.append(f"⚠️  {len(untracked_files)} archivo(s) no rastreado(s):")
        for f in untracked_files[:5]:
            messages.append(f"   - {f}")
        if len(untracked_files) > 5:
            messages.append(f"   ... y {len(untracked_files) - 5} más")
    elif untracked_files and not strict:
        messages.append(f"ℹ️  {len(untracked_files)} archivo(s) no rastreado(s) (usa --strict para incluir en la verificación)")
    
    if has_uncommitted:
        message = "❌ Cambios sin commitear detectados:\n" + "\n".join(messages)
        message += "\n\n💡 Sugerencias:"
        message += "\n   1. Commitea los cambios: git add . && git commit -m 'mensaje'"
        message += "\n   2. Descarta los cambios: git restore ."
        message += "\n   3. Guarda temporalmente: git stash"
        return True, message
    else:
        return False, "✅ No hay cambios sin commitear"


def main():
    """Función principal del script."""
    strict_mode = '--strict' in sys.argv
    
    has_changes, message = check_uncommitted_changes(strict=strict_mode)
    
    print(message)
    
    if has_changes:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
