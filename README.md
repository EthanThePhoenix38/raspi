# Raspi - Configuration Basique à Distance

[![CI/CD Pipeline](https://github.com/EthanThePhoenix38/raspi/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/EthanThePhoenix38/raspi/actions)
[![codecov](https://codecov.io/gh/EthanThePhoenix38/raspi/branch/main/graph/badge.svg)](https://codecov.io/gh/EthanThePhoenix38/raspi)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Un outil de configuration basique pour Raspberry Pi avec déploiement automatisé et vérifications de sécurité.

## Fonctionnalités

- ✅ Configuration automatique des systèmes Raspberry Pi
- 🔒 Vérifications de sécurité intégrées (bandit, safety)
- 🧹 Formatage automatique du code (black, flake8)
- 📝 Vérification de types (mypy)
- 🚀 Déploiement automatique avec versioning sémantique
- 📦 Publication automatique sur PyPI
- 🔄 Pull requests automatiques
- ✨ Hooks pre-commit pour la qualité du code

## Installation

```bash
# Installation depuis PyPI
pip install raspi

# Installation pour le développement
git clone https://github.com/EthanThePhoenix38/raspi.git
cd raspi
pip install -e .[dev]
```

## Utilisation

```python
from raspi.main import get_system_info

# Obtenir les informations système
info = get_system_info()
print(info)
```

Ou depuis la ligne de commande:

```bash
python -m raspi.main
```

## Développement

### Configuration de l'environnement

```bash
# Cloner le repo
git clone https://github.com/EthanThePhoenix38/raspi.git
cd raspi

# Installer les dépendances de développement
pip install -r requirements-dev.txt
pip install -e .

# Configurer les hooks pre-commit
pre-commit install
```

### Tests

```bash
# Exécuter les tests
pytest

# Avec couverture
pytest --cov=src/raspi --cov-report=html
```

### Vérifications de qualité

```bash
# Formatage du code
black src/ tests/

# Linting
flake8 src/ tests/

# Vérification de types
mypy src/

# Vérifications de sécurité
bandit -r src/
safety check
```

## CI/CD et Versioning

Ce projet utilise:

- **GitHub Actions** pour l'intégration continue
- **Semantic Versioning** pour le versioning automatique
- **Pre-commit hooks** pour la qualité du code
- **Publication automatique** sur PyPI lors des releases

### Workflow de contribution

1. Créer une branche depuis `main`
2. Effectuer les modifications
3. Push de la branche → création automatique d'une pull request
4. Merge vers `main` → tests, build, et release automatique si nécessaire

### Format des commits

Utiliser [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: ajout d'une nouvelle fonctionnalité
fix: correction d'un bug
docs: mise à jour de la documentation
style: formatage du code
refactor: refactorisation du code
test: ajout ou modification de tests
chore: tâches de maintenance
```

## Sécurité

- **Bandit**: Analyse statique de sécurité du code Python
- **Safety**: Vérification des vulnérabilités dans les dépendances
- **Pre-commit hooks**: Vérifications automatiques avant chaque commit

## Licence

MIT License - voir [LICENSE](LICENSE) pour les détails.
