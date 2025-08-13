#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import subprocess
import janela
import tree
import sys

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
	time_log = datetime.now().strftime("log_A_%Y_M_%m_D_%d_H_%H_M_%M_.log")
	file_log = Path(time_log).expanduser().resolve()
	list_dir = tree.result()
	if not file_log.exists():
		file_log.touch(exist_ok=True)
	elif file_log.is_file():
		with open(file_log, mode='a', encoding='', newline='') as log:
			log.writelines(f"{datetime.now().strftime('%Y-%d-%m %H:%M:%S')}\n \
{commit}\n{list_dir}\n\n")
	else:
		sys.exit(1)

def	verif_caminho():
	dir_oculto = ".";
	path = Path(dir_oculto + "git").expanduser().resolve()

	if path.is_dir():
		print (f"Pasta git identificada: {path.resolve()}")
		commit = janela.msg_commit()
		make_add()
		make_commit(commit)
		make_push()
		criar_log(commit)
	else:
		print ("Pasta git não identificado!\
\n Certifica que esta rodando no Diretorio raiz")
		sys.exit(1)

if __name__ == "__main__":
	verif_caminho()
