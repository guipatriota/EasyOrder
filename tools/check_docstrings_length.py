"""Verificador de tamanho de docstrings para o projeto EasyOrder.

Percorre arquivos Python em 'src/' e 'tests/' e garante que a primeira linha
das docstrings tenha pelo menos MIN caracteres. Pode ser executado via CLI.
"""

import ast
import sys
from pathlib import Path

MIN = 15  # tamanho mínimo da 1ª linha da docstring


def check_file(path: Path) -> list[str]:
    """Verifica docstrings de um arquivo Python específico.

    Analisa o AST do arquivo e valida se as docstrings do módulo, classes e
    funções possuem a primeira linha com pelo menos MIN caracteres.

    Args:
        path (Path): Caminho do arquivo Python a ser verificado.

    Returns:
        list[str]: Lista de mensagens de erro encontradas; vazia se não houver.
    """
    errs = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"{path}: erro ao parsear: {e}")
        return errs

    # módulo
    mod_doc = ast.get_docstring(tree, clean=True)
    if not mod_doc or len(mod_doc.splitlines()[0]) < MIN:
        errs.append(
            f"{path}: docstring de módulo ausente ou 1ª linha < {MIN} chars"
        )

    # classes e defs
    for node in ast.walk(tree):
        if isinstance(
            node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        ):
            doc = ast.get_docstring(node, clean=True)
            kind = (
                "função"
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                else "classe"
            )
            if not doc or len(doc.splitlines()[0]) < MIN:
                errs.append(
                    f"{path}:{node.lineno} {kind} '{node.name}': "
                    + f"docstring ausente ou 1ª linha < {MIN} chars"
                )
    return errs


def main() -> int:
    """Executa o verificador de docstrings via interface de linha de comando.

    Percorre as pastas 'src' e 'tests', reporta problemas e retorna código de
    saída adequado para uso em CI.

    Returns:
        int: 0 se todas as docstrings forem válidas; 1 caso contrário.
    """
    roots = [Path("src"), Path("tests")]
    errs: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for py in root.rglob("*.py"):
            errs.extend(check_file(py))
    if errs:
        print("\n".join(errs))
        return 1
    print("Docstrings OK (mínimo de caracteres atendido).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
