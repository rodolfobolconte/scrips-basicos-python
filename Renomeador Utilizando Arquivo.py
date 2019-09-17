import os

#CAMINHO COMPLETO DA PASTA COM '/' NO FINAL
pasta = "A:/Downloads/teste/"
#CAMINHO COMPLETO DO ARQUIVO COM OS NOMES, INCLUINDO O NOME DO ARQUIVO
arquivo = open("A:/Downloads/Renomeador Utilizando Arquivo - Arquivo.txt", "r", encoding="utf-8")
#EXTENSÃO DOS ARQUIVOS
extensao = "txt"

nomes = arquivo.readlines()
for i in range(len(nomes)):
    nomes[i] = nomes[i].replace("\n", "")

for (nome_do_arquivo_antigo, nome_do_arquivo_novo) in zip(sorted(os.listdir(pasta), key=len), nomes):
    os.rename(pasta + nome_do_arquivo_antigo, "%s%s.%s" %(pasta, nome_do_arquivo_novo, extensao))