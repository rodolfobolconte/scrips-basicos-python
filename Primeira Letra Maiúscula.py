while True:
    texto = input('Digite um texto para converter em maiúsculo (0: sair): ')
    if texto == '0':
        break

    texto = texto.lower().split()

    for i in range(len(texto)):
        texto[i] = texto[i][0].upper() + texto[i][1:]

    print(texto)
    print(' '.join(texto))