#!/usr/bin/env python3

import os
import time
import subprocess
from pathlib import Path
from make_commit import make_all

DIRETORIO = Path().expanduser().resolve()
MIN_LINHAS = 20
TIME_VAR = 60

def mudou_significativamente():
    diff = subprocess.run(
        ["git", "diff", "-w", "--unified=0", "--ignore-blank-lines", "--ignore-space-change", "HEAD"],
        cwd=DIRETORIO,
        capture_output=True,
        text=True
    ).stdout.splitlines()

    linhas_mod = [
        l for l in diff
        if (l.startswith("+") or l.startswith("-"))
        and not l.startswith(("+++", "---"))
        and l[1:].strip() != "" 
    ]
    return len(linhas_mod) >= MIN_LINHAS

def monitorar(diretorio):
    while True:
        if mudou_significativamente():
            make_all()
            time.sleep(TIME_VAR) 
        time.sleep(TIME_VAR)

if __name__ == "__main__":
    if not DIRETORIO.is_dir():
        print(f"Diretório não encontrado: {DIRETORIO}")
    else:
        monitorar(DIRETORIO)
