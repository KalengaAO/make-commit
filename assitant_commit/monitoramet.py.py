#!/usr/bin/env python3

import os
import time
import subprocess
from pathlib import Path
from make_commit import make_all

DIRETORIO = Path().expanduser().resolve()
MIN_LINHAS = 2  # mínimo de linhas alteradas (adição + remoção) para acionar

def mudou_significativamente():
    # Pega diff ignorando espaços (-w) e sem contexto (--unified=0)
    diff = subprocess.run(
        ["git", "diff", "-w", "--unified=0", "HEAD"],
        cwd=DIRETORIO,
        capture_output=True,
        text=True
    ).stdout.splitlines()

    linhas_mod = [
        l for l in diff
        if (l.startswith("+") or l.startswith("-"))
        and not l.startswith(("+++", "---"))  # ignora cabeçalhos do patch
        and l[1:].strip() != ""               # ignora linhas vazias
    ]
    return len(linhas_mod) >= MIN_LINHAS

def monitorar(diretorio):
    while True:
        if mudou_significativamente():
            make_all()
            time.sleep(5)  # cooldown para evitar commits repetidos
        time.sleep(10)

if __name__ == "__main__":
    if not DIRETORIO.is_dir():
        print(f"Diretório não encontrado: {DIRETORIO}")
    else:
        monitorar(DIRETORIO)
