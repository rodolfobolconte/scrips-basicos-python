import os

#CAMINHO COMPLETO DA PASTA COM '/' NO FINAL
pasta = "A:/Downloads/teste/"

#INÍCIO DA CONTAGEM
numero = 100
#EXTENSÃO DOS ARQUIVOS
extensao = "txt"

for nome_do_arquivo in sorted(os.listdir(pasta), key=len):
	os.rename(pasta + nome_do_arquivo, pasta + "1 (%d).%s" %(numero, extensao))
	numero += 1