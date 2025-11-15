"""
Tests para el módulo check_uncommitted_changes.

Verifica que el detector de cambios sin commitear funcione correctamente.
"""

import unittest
import subprocess
import tempfile
import os
import shutil
from pathlib import Path
import sys

# Agregar el directorio utils al path para importar el módulo
sys.path.insert(0, str(Path(__file__).parent))

from check_uncommitted_changes import check_uncommitted_changes, run_git_command


class TestCheckUncommittedChanges(unittest.TestCase):
    """Tests para la función check_uncommitted_changes."""
    
    def setUp(self):
        """Crear un repositorio git temporal para las pruebas."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        # Inicializar repositorio git
        subprocess.run(['git', 'init'], capture_output=True, check=True)
        subprocess.run(['git', 'config', 'user.email', 'test@example.com'], capture_output=True, check=True)
        subprocess.run(['git', 'config', 'user.name', 'Test User'], capture_output=True, check=True)
        
        # Crear commit inicial
        Path('README.md').write_text('# Test Repo')
        subprocess.run(['git', 'add', 'README.md'], capture_output=True, check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], capture_output=True, check=True)
    
    def tearDown(self):
        """Limpiar el repositorio temporal."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_no_changes(self):
        """Test: repositorio limpio sin cambios."""
        has_changes, message = check_uncommitted_changes()
        self.assertFalse(has_changes)
        self.assertIn('✅', message)
        self.assertIn('No hay cambios', message)
    
    def test_modified_file(self):
        """Test: detectar archivo modificado."""
        # Modificar archivo existente
        Path('README.md').write_text('# Modified content')
        
        has_changes, message = check_uncommitted_changes()
        self.assertTrue(has_changes)
        self.assertIn('❌', message)
        self.assertIn('modificado', message.lower())
    
    def test_staged_changes(self):
        """Test: detectar cambios en staging."""
        # Crear y agregar nuevo archivo
        Path('new_file.txt').write_text('New content')
        subprocess.run(['git', 'add', 'new_file.txt'], capture_output=True, check=True)
        
        has_changes, message = check_uncommitted_changes()
        self.assertTrue(has_changes)
        self.assertIn('❌', message)
        self.assertIn('staging', message.lower())
    
    def test_untracked_file_non_strict(self):
        """Test: archivo no rastreado en modo no estricto."""
        # Crear archivo no rastreado
        Path('untracked.txt').write_text('Untracked content')
        
        has_changes, message = check_uncommitted_changes(strict=False)
        # En modo no estricto, archivos no rastreados no cuentan como cambios
        self.assertFalse(has_changes)
        self.assertIn('✅', message)
    
    def test_untracked_file_strict(self):
        """Test: archivo no rastreado en modo estricto."""
        # Crear archivo no rastreado
        Path('untracked.txt').write_text('Untracked content')
        
        has_changes, message = check_uncommitted_changes(strict=True)
        # En modo estricto, archivos no rastreados cuentan como cambios
        self.assertTrue(has_changes)
        self.assertIn('❌', message)
        self.assertIn('no rastreado', message.lower())
    
    def test_run_git_command(self):
        """Test: ejecutar comando de git."""
        returncode, stdout, stderr = run_git_command(['git', 'status', '--porcelain'])
        self.assertEqual(returncode, 0)
        self.assertIsInstance(stdout, str)
        self.assertIsInstance(stderr, str)


class TestNonGitDirectory(unittest.TestCase):
    """Tests para verificar comportamiento fuera de un repositorio git."""
    
    def setUp(self):
        """Crear un directorio temporal sin git."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
    
    def tearDown(self):
        """Limpiar el directorio temporal."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_not_a_git_repo(self):
        """Test: detectar cuando no es un repositorio git."""
        has_changes, message = check_uncommitted_changes()
        self.assertTrue(has_changes)
        self.assertIn('❌', message)
        self.assertIn('repositorio Git', message)


if __name__ == '__main__':
    unittest.main()
