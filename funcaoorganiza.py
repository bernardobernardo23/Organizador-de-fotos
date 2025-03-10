import os   # manipulação de arquivos
import shutil #mover arquivos entre pastas
import re #identificação de padroes nos nomes dos arq

desorganizada = r"C:\Users\Pichau\Desktop\testeorganizacao" #r --> raw string --> para evitar problemas com \

extensoes = {".jpg", ".jpeg", ".png", ".mp4"}

pasta_outros = os.path.join(desorganizada, "Outros") #cria uma pasta outros dentro do diretorio da variavel organizada
os.makedirs(pasta_outros, exist_ok=True) #se nao existir ele cria

padraonome = re.compile(r"^(\d{4})\d{4}_\d{6}") #padrao do nome dos arquivos 20161011_200235.jpg
                                                                            #YYYYMMDD_HHMMSS

for arquivo in os.listdir(desorganizada): #para cada arquivo na pasta 
    caminho_arquivo = os.path.join(desorganizada, arquivo) # caminho completo,por exemplo:("c:\fotos","foto.png")

    if os.path.isfile(caminho_arquivo): #verifica que o arquivo se trata de um arquivo e nao uma pasta
        extensao = os.path.splitext(arquivo)[1].lower() #splitext -->separa o arquivo entre nome e extensao, por meio do .
                                                        #retorna ("foto",".png")--> [1]=.png --> pega so a extensao
                                                        #.lower() -- > manda para letra minuscula -- JPG --> jpg
        if extensao in extensoes:
            match = padraonome.match(arquivo) #verifica se o nome do arquivo bate com o padrao

            if match:
                ano = match.group(1)  # captura o ano do nome do arquivo 
                pasta_destino = os.path.join(desorganizada, ano) #manda para a respectiva pasta
            else:
                pasta_destino = pasta_outros  # se n bater manda pra outros
                
            os.makedirs(pasta_destino, exist_ok=True) # criar a pasta de destino, se não existir
                # makedirs - cria pastas
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo)) # mover o arquivo para a pasta correspondente

print("Organização concluída!")
