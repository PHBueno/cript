qntd_bytes_bloco = 8


def bloco(cifra: list):
    blc = dict()
    _cifra = cifra
    count = 0
    while count <= len(_cifra):
        blc[f"{count}"] = list()
        for i in range(0, 8):
            blc[f"{count}"].append(_cifra[i])
        del (_cifra[0:8])
        count += 1
    return blc


def decifra(cifra: list, chave: list, vi: list):
    blocos = bloco(cifra)
    for b in blocos:

        proximo_xor = [((int(vi[i]) * chave[i]) % 256) for i in range(0, qntd_bytes_bloco)]
        decif = [int(blocos[b][i]) ^ proximo_xor[i] for i in range(0, len(blocos[b]))]
        vi = blocos[b]
        blocos[b] = [chr(i) for i in decif if chr(i) != chr(7)]  # Mensagem decifrada removendo os bytes de controle
    return blocos


if __name__ == "__main__":
    vetor_inicial = [i+20 for i in range(0, qntd_bytes_bloco)]

    cifra = str(input("Informe a cifra: ")).split(" ")

    print("\nEntre com a chave: 8 valores menores que 256.\n")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, qntd_bytes_bloco)]

    _decifra = decifra(cifra=cifra, chave=chave, vi=vetor_inicial)

    for b in _decifra:
        for l in _decifra[b]:
            print(l, end='')
    print('\n')
