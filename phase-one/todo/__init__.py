"""
Bridge package so `python -m todo` works from the repository root without
installing the project. Submodules are loaded from src/todo.
"""

import sys
from pathlib import Path

_pkg_dir = Path(__file__).resolve().parent
_src_pkg = _pkg_dir.parent / "src" / "todo"

if _src_pkg.parent.exists():
    sys.path.insert(0, str(_src_pkg.parent))
    __path__ = [str(_pkg_dir), str(_src_pkg)]
else:
    __path__ = [str(_pkg_dir)]

from todo.cli import main  # type: ignore  # imported from src/todo via adjusted path

__all__ = ["main"]
