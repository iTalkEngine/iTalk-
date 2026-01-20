from pathlib import Path
import json
import ast
import typer
from rich.console import Console
from .rules import detect_long_functions, detect_unused_imports

app = typer.Typer(help="PyRefactor — analyse et refactorisation Python (CLI)")
console = Console()


@app.command()
def scan(path: Path = typer.Argument(..., help="Dossier ou fichier à scanner"),
         min_func_lines: int = typer.Option(50, help="Seuil lignes pour fonctions longues"),
         output: Path | None = typer.Option(None, help="Fichier JSON de sortie")):
    """Scanner le code et afficher les problèmes détectés."""
    files = []
    if path.is_file() and path.suffix == ".py":
        files = [path]
    else:
        files = list(path.rglob("*.py"))
    results = []
    for f in files:
        try:
            src = f.read_text(encoding="utf-8")
            tree = ast.parse(src)
            long_funcs = detect_long_functions(tree, min_func_lines)
            unused = detect_unused_imports(tree)
            if long_funcs or unused:
                results.append({"file": str(f), "long_functions": long_funcs, "unused_imports": unused})
        except Exception as e:
            console.log(f"[red]Erreur en lisant {f}: {e}[/red]")
    if not results:
        console.print("[green]Aucun problème détecté.[/green]")
    else:
        for r in results:
            console.rule(r["file"])
            if r["long_functions"]:
                console.print("[bold yellow]Fonctions longues:[/bold yellow]")
                for lf in r["long_functions"]:
                    console.print(f" - {lf}")
            if r["unused_imports"]:
                console.print("[bold yellow]Imports non utilisés:[/bold yellow]")
                for ui in r["unused_imports"]:
                    console.print(f" - {ui}")
    if output:
        output.write_text(json.dumps(results, indent=2, ensure_ascii=False))


@app.command()
def apply(rule: str = typer.Option(..., help="Nom de la règle à appliquer"),
          path: Path = typer.Option(..., help="Fichier ou dossier"),
          apply_changes: bool = typer.Option(False, "--apply", help="Appliquer les changements (sinon dry-run)")):
    """Appliquer un refactor simple. Pour l'instant: 'organize-imports' (placeholder)."""
    console.print(f"Règle demandée: {rule} sur {path} (apply={apply_changes})")
    # Placeholder: implémenter codemods via LibCST
    console.print("[yellow]Feature en développement — codemods à implémenter[/yellow]")


if __name__ == "__main__":
    app()
