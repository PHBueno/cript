mod = 256
bytes_por_bloco = 8


def invModular(chave: int) -> int:
    _chave = chave
    inverso = int
    for prox in range(0, mod-1):
        inv = (_chave * prox) % mod
        if inv == 1:
            inverso = prox
            break
    return inverso


def bloco(cifra: list):
    blc = dict()
    _cifra = cifra
    count = 0
    while count <= len(_cifra):  # 0 <= 8;
        blc[f"{count}"] = list()
        for i in range(0, 8):
            blc[f"{count}"].append(_cifra[i])
        del (_cifra[0:8])
        count += 1
    return blc


def decifra(cifra: list, chave: list, vi: list):
    blocos = bloco(cifra)
    proximo_xor = vi
    blocos_decif = {}
    for b in blocos:
        blocos_decif[b] = list()
        for c in range(0, len(blocos[b])):
            decif = (int(blocos[b][c]) * chave[c]) % mod
            xor = decif ^ int(proximo_xor[c])
            if chr(xor) != chr(7):
                blocos_decif[b].append(chr(xor))
        proximo_xor = [i for i in blocos[b]]
    return blocos_decif


if __name__ == "__main__":
    cifra = str(input("Informe a cifra separada por espaço: ")).split(" ")

    vetor_inicial = [i+20 for i in range(0, 8)]

    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]
    chave_invMod = [invModular(c) for c in chave]
    _decifra = decifra(cifra=cifra, vi=vetor_inicial, chave=chave_invMod)

    for b in _decifra:
        for l in _decifra[b]:
            print(l, end='')
    print('\n')

    # print(f"Blocos: {_decifra}")
