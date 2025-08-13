#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import subprocess
import sys
import janela
import tree

RED = "\033[1;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
RESET = "\033[0m"

def	make_add():
	subprocess.run(
			["git", "add", "."],
			check=True,
			stdout=subprocess.DEVNULL)

def	make_commit(commit):
	subprocess.run([
			"git", "commit", "-m", commit],
			check=True,
			stdout=subprocess.DEVNULL)

def	make_push():
	subprocess.run(["git", "push"],
			check=True,
			stdout=subprocess.DEVNULL)

def	criar_log(commit):
	time_log = "../logcommit.log"
	file_log = Path(time_log).expanduser().resolve()
	list_dir = tree.result()
	if not file_log.exists():
		file_log.touch(exist_ok=True)
	if file_log.is_file():
		with open(file_log, mode='a', encoding='utf-8', newline='') as log:
			log.write(f"Data: {datetime.now().strftime('%Y-%d-%m %H:%M:%S')}\n"
						f"commit feito: {commit}\n"
						f"Arquivos e diretorio:\n {list_dir}\n\n")
	else:
		sys.exit(1)

def	make_all():
	dir_oculto = ".";
	path = Path(dir_oculto + "git").expanduser().resolve()
	print (path)
	if path.is_dir():
		print (f"Pasta git identificada: {path.resolve()}")
		commit = janela.msg_commit()
		if commit:
			make_add()
			make_commit(commit)
			make_push()
			criar_log(commit)
		else:
			print (f"{YELLOW}Nenhum commit feito!{RESET}")
			return
	else:
		print (f"{RED}Pasta git não identificado!\
\nCertifica que esta rodando o script no Diretorio raiz do projecto!{RESET}")
		sys.exit(1)

if __name__ == "__main__":
	make_all()
