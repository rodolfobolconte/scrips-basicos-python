import os

#CAMINHO COMPLETO DA PASTA COM '/' NO FINAL
pasta = "A:/Downloads/teste/"

#INÍCIO DA CONTAGEM
numero = 1
#EXTENSÃO DOS ARQUIVOS
extensao = "txt"

for nome_do_arquivo in sorted(os.listdir(pasta), key=len):
    os.rename(pasta + nome_do_arquivo, "%s%d - %s.%s" %(pasta, numero, nome_do_arquivo, extensao))
    numero += 1