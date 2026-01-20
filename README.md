# PyRefactor — Outil d'analyse & refactorisation Python (CLI / TUI)

PyRefactor est un outil open‑source pour analyser, détecter et appliquer des refactorings simples sur du code Python. Conçu pour améliorer la qualité du code et l'expérience développeur (DX) : CLI rapide, sorties lisibles (Rich), mode dry‑run et possibilité d'interface TUI/GUI ultérieure.

Principes
- Focus sur règles pratiques et non intrusives : détection d'anti‑patterns courants et suggestions de refactor.
- Mode "dry-run" pour revoir les modifications avant application.
- Extensible : règles additionnelles plug‑inables.

MVP (v0)
- CLI `pyrefactor scan <path>` : détecte fonctions trop longues (> N lignes), imports non utilisés, variables mal nommées simples.
- Commande `pyrefactor apply --rule <rule>` : applique un refactorage simple (ex : organiser imports, formater).
- Rapports en console (Rich) et export JSON.
- Tests de base et CI (GitHub Actions).

Stack recommandé
- Python 3.11+
- Typer (CLI), Rich (affichage), LibCST / ast (analyse & codemods)
- Pytest pour tests
- Optional: Textual ou Streamlit pour UI

Installer (dev)
1. Cloner le repo
2. Créer un environnement virtuel :
   python -m venv .venv
   source .venv/bin/activate
3. Installer :
   pip install -e .

Usage
- Scanner un dossier :
  pyrefactor scan path/to/project
- Scanner avec export JSON :
  pyrefactor scan path/to/project --output report.json
- Appliquer une règle (dry-run par défaut) :
  pyrefactor apply --rule long-functions --apply
- Aide :
  pyrefactor --help

Contribuer
- Lire CONTRIBUTING.md et CODE_OF_CONDUCT.md
- Créer une issue pour proposer une nouvelle règle ou un refactor
- Tests → CI passe → PR

Roadmap rapide
- v0.1 : détections de base + CLI
- v0.2 : codemods avec LibCST, apply automatique avec rollback
- v0.3 : TUI (Textual) et intégration pre-commit
- v1.0 : plugin rules marketplace, règles communautaires

Licence
MIT — voir LICENSE
