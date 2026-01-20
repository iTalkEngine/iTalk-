import ast
from typing import List

def detect_long_functions(tree: ast.AST, min_lines: int = 50) -> List[str]:
    """Retourne une liste de descriptions de fonctions dont le nombre de lignes dépasse min_lines."""
    results = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if hasattr(node, "end_lineno") and node.end_lineno and node.lineno:
                length = node.end_lineno - node.lineno + 1
                if length >= min_lines:
                    qualname = node.name
                    results.append(f"{qualname} (lignes: {length}, start: {node.lineno})")
    return results

def detect_unused_imports(tree: ast.AST) -> List[str]:
    """Détection très simple d'imports non utilisés — heuristique basée sur noms."""
    imports = {}
    used_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                imports[alias.asname or alias.name] = f"{module}.{alias.name}"
        elif isinstance(node, ast.Name):
            used_names.add(node.id)
    unused = []
    for asname, fullname in imports.items():
        # si le nom importé n'apparait pas dans used_names → potentiellement non utilisé
        base = asname.split(".")[0]
        if base not in used_names:
            unused.append(fullname)
    return unused
