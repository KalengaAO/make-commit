#!/usr/bin/env python3

import os
import time
import subprocess
from pathlib import Path
from make_commit import make_all

DIRETORIO = Path().expanduser().resolve()
MIN_LINHAS = 20
TEMPO_VER = 60

def mudou_sign():
    diff = subprocess.run(
        [
            "git", "diff", "-w", "--unified=0",
            "--ignore-blank-lines", "--ignore-space-change", "HEAD"
        ],
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
    return len(linhas_mod)

def monitorar(diretorio):
    while True:
        cmd = str(input("Prima ok para commit: ")).lower().strip()
        if cmd == "ok":
            if mudou_sign() >= MIN_LINHAS:
                make_all()
                time.sleep(TEMPO_VER)
        cmd = None
        print ("Número de linhas verificadas:", mudou_sign())

if __name__ == "__main__":
    if not DIRETORIO.is_dir():
        print(f"Diretório não encontrado: {DIRETORIO}")
    else:
        monitorar(DIRETORIO)

