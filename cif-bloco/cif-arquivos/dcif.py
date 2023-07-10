import os
mod = 256


def invModular(chave: int) -> int:
    _chave = chave
    inverso = int
    for prox in range(0, mod-1):
        inv = (_chave * prox) % mod
        if inv == 1:
            inverso = prox
            break
    return inverso


def bloco(cifra: str, chave: list):
    aux = list()
    aux2 = str()
    fim = inicio = 0
    controle = 0
    _cifra = cifra
    for i in range(0, 8):  # Decifra o primeiro bloco
        if cifra[i] != chr(7):
            aux2 += str(chr((ord(cifra[i]) * chave[i]) % mod))
    aux.append(aux2)
    _cifra = cifra[8:]  # Copia do primeiro bloco para frente (primeiro bloco já decifrado)
    while controle <= len(_cifra) - 1:
        fim += 8
        aux.append(_cifra[inicio:fim])
        inicio += 8
        controle += 1
        if inicio >= len(_cifra): break
    return aux


def decifra(cifra: str, chave: list, arq_saida):
    blocos = bloco(cifra=cifra, chave=chave)
    with open(arq_saida, 'x') as file:
        file.write(blocos[0].replace('-', ' '))  # Escreve o primeiro bloco
        del blocos[0]  # Deleta o primeiro bloco (já inserido do arquivo)
        for b in blocos:  # Processa o restante dos blocos
            count = 0
            for ltr in b:
                cif = (ord(ltr) * chave[count]) % mod
                temp = chr(cif).replace('-', ' ').replace('$', '\n')
                file.write(temp)
                count += 1


if __name__ == '__main__':
    arq_entrada = str(input("Arquivo de entrada: "))
    arq_saida = str(input("Arquivo de saída: "))

    arq_1 = open(arq_entrada, "r")
    cifra = arq_1.read()
    arq_1.close()

    tamanho = os.stat(arq_entrada).st_size  # Tamanho, em bits, do arquivo
    qntd_blocos = int(tamanho / 8)
    print('\n')
    print("=-" * 9)
    print("Informe valores ímpares para as chaves\n")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]
    print("=-" * 9)
    chave_invMod = [invModular(c) for c in chave]

    decifra(cifra=cifra, chave=chave_invMod, arq_saida=arq_saida)

    print("\n!! Processamento finalizado !!\n")



