#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as msgbox

def	msg_commit():
	make = "Make commit com git assistente >_"
	prompt = "Prima <Enter / submiter> ou <Esc / cancelar>"
	msg = {"value": None}
	janela = tk.Tk()
	janela.title(make)
	tk.Label(janela, text=prompt).pack(pady=5)
	janela.geometry("490x150")
	janela.resizable(False, False)

	def	submeter(event=None):
		val = entrada.get().strip()
		if not val:
			msgbox.showwarning("Sério!", "Não submeta commit vazio Cadete!")
			return
		msg["value"] = val
		janela.destroy()

	def	cancelar(event=None):
		janela.destroy()

	entrada = tk.Entry(janela, width=50)
	entrada.pack(pady=5)
	entrada.focus()
	botao = tk.Frame(janela)
	botao.pack(pady=10)
	tk.Button(botao, text="confirmar", command=submeter).pack(side="left", padx=5)
	tk.Button(botao, text="Cancelar", command=cancelar).pack(side="left", padx=5)

	janela.bind("<Return>", submeter)
	janela.bind("<Escape>", cancelar)

	janela.mainloop()
	return msg["value"]

def	main():
	commit = msg_commit()
	
if __name__ == "__main__":
	main()
