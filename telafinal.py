import os
import shutil
import re
import tkinter as tk
from tkinter import filedialog, messagebox

extensoes = {".jpg", ".jpeg", ".png", ".mp4"}

def organizar_fotos(desorganizada):
    if not desorganizada:
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta primeiro.") #caso aperte pra organizar sem dar um diretorio
        return

    pasta_outros = os.path.join(desorganizada, "Outros")
    os.makedirs(pasta_outros, exist_ok=True)

    padraonome = re.compile(r"^(\d{4})\d{4}_\d{6}")

    for arquivo in os.listdir(desorganizada):
        caminho_arquivo = os.path.join(desorganizada, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao in extensoes:
                match = padraonome.match(arquivo)

                if match:
                    ano = match.group(1)
                    pasta_destino = os.path.join(desorganizada, ano)
                else:
                    pasta_destino = pasta_outros
                    
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

    messagebox.showinfo("Sucesso", "Organização concluída!")

janela = tk.Tk() #criacao da janela
janela.title("Organizador de Fotos")  
janela.geometry("400x200")
janela.resizable(False,False) #n deixa redimensionar na largura nem altura

entrada_caminho = tk.Entry(janela, width=50)  # Campo de texto para exibir a pasta selecionada
entrada_caminho.pack(pady=10) #tk.entry -> input text || .pack() -coloca o elemento na janela ||pady = padding

def selecionar_pasta():
    pasta = filedialog.askdirectory()  # abre o explorador de arquivos para selecionar a pasta
    if pasta:
        entrada_caminho.delete(0, tk.END)  # limpa o campo de texto caso esteja escrito algo
        entrada_caminho.insert(0, pasta)  # insere o caminho da pasta no campo de texto

botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)  #chama a funcao selecionar pasta
botao_selecionar.pack(pady=5)

def iniciar_organizacao():
    caminho = entrada_caminho.get()  # caminho da pasta
    organizar_fotos(caminho)  # manda o caminho da desorganizada pra função principal 

botao_organizar = tk.Button(janela, text="Organizar Fotos", command=iniciar_organizacao)
botao_organizar.pack(pady=10)

janela.mainloop() #abre a janela
