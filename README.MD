# Scripts Básicos Python

Repositório com Scripts para a manipulação e organização de Strings e Arquivos do Windows.

## Contribuição

Se você gostou do Repositório e deseja contribuir para que os Scripts criados sejam aprimorados, ou até corrigir um eventual erro, sinta-se à vontade para fazer um Pull Request do Repositório :grin:   

## Lista de Scripts

### [Inserir Números em Nomes de Arquivos](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Inserir%20N%C3%BAmeros%20em%20Nomes%20de%20Arquivos.py)

Dado os arquivos de uma pasta do Windows, o Script coloca um número no início do nome e segue em sequência até o último arquivo, por exemplo, arquivos de uma pasta com os nomes:

Nome Original | Nome Após Script
:-:|:-:
Chinese Democracy.mp3 | 1 - Chinese Democracy.mp3
Shackler's Revenge.mp3 | 2 - Shackler's Revenge.mp3

É necessário informar:

- O caminho completo da pasta com os arquivos, desde a partição na qual ela se encontra até um ```/``` no final, por exemplo  ```A:/Downloads/scripts-basicos-python/```;
- O primeiro valor da sequência numérica na variável `numero`;
- A extensão dos arquivos, sem o ```.```, por exemplo ```mp3```, na variável `extensao`.

### [Palavras Maiúsculas](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Palavras%20Mai%C3%BAsculas.py)

Um loop infinito para inserir uma string de caracteres, retornando os mesmos como maiúsculos, por exemplo:

String Inserida | String Transformada
:-:|:-:
Meu Nome Maiúsculo | MEU NOME MAIÚSCULO
outro exemplo | OUTRO EXEMPLO

Basta executar o script e inserir as Strings.

### [Palavras Minúsculas](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Palavras%20Min%C3%BAsculas.py)

Um loop infinito para inserir uma string de caracteres, retornando os mesmos como minúsculos, por exemplo:

String Inserida | String Transformada
:-:|:-:
Meu Nome minúsculo | meu nome minúsculo
OUTRO EXEMPLO | outro exemplo

Basta executar o script e inserir as Strings.

### [Primeira Letra Maiúscula](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Primeira%20Letra%20Mai%C3%BAscula.py)

Um loop infinito para inserir uma string de caracteres, retornando a primeira letra de cada palavra como maiúscula, por exemplo:

String Inserida | String Transformada
:-:|:-:
meu nome por exemplo | Meu Nome Por Exemplo
OUTRO EXEMPLO | Outro Exemplo

Basta executar o script e inserir as Strings.

### [Renomeador de Arquivos por Pasta](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Renomeador%20de%20Arquivos%20por%20Pasta.py)

Dado os arquivos de uma pasta do Windows, o Script renomeia os arquivos com o nome `1` seguido de uma sequência numérica até o último arquivo, por exemplo, arquivos de uma pasta com os nomes:

Nome Original | Nome Após Script
:-:|:-:
Chinese Democracy.mp3 | 1 (1).mp3
Shackler's Revenge.mp3 | 1 (2).mp3

É necessário informar:

- O caminho completo da pasta com os arquivos, desde a partição na qual ela se encontra até um ```/``` no final, por exemplo  ```A:/Downloads/scripts-basicos-python/```;
- O primeiro valor da sequência numérica na variável `numero`;
- A extensão dos arquivos, sem o ```.```, por exemplo ```mp3```, na variável `extensao`.

### [Renomeador Utilizando Arquivo](https://github.com/rodolfobolconte/scripts-basicos-python/blob/master/Renomeador%20Utilizando%20Arquivo.py)

Dado os arquivos de uma pasta do Windows, o Script renomeia os arquivos de acordo com os nomes inseridos no arquivo ```Renomeador Utilizando Arquivo - Arquivo.txt```, por exemplo, arquivos de uma pasta com os nomes:

Nome Original | Nome no Arquivo.txt | Nome Após Script
:-:|:-:|:-:
Chinese Democracy.mp3 | Música 1 | Música 1.mp3
Shackler's Revenge.mp3 | Música 2 | Música 2.mp3

É necessário informar:

- O caminho completo da pasta com os arquivos, desde a partição na qual ela se encontra até um ```/``` no final, por exemplo  ```A:/Downloads/scripts-basicos-python/```;
- O caminho completo do Arquivo.txt com os novos nomes, mais o nome deste arquivo, por exemplo ```A:/Downloads/scripts-basicos-python/Renomeador Utilizando Arquivo - Arquivo.txt``` na variável ```arquivo```;
- O primeiro valor da sequência numérica na variável `numero`;
- A extensão dos arquivos, sem o ```.```, por exemplo ```mp3```, na variável `extensao`.