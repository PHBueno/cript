caracteres = 8  # quantidade de caracteres por bloco = blocos de 64 bits
mod = 256


def blocos(cifra: list) -> dict:
    m = dict()
    _cifra = cifra
    count = 0
    while count <= len(_cifra):  # 0 <= 8;
        m[f"{count}"] = list()
        for i in range(0, caracteres):
            m[f"{count}"].append(_cifra[i])
        del(_cifra[0:8])
        count += 1
    return m


def invModular(chave: int) -> int:
    _chave = chave
    inverso = int
    for prox in range(0, mod-1):
        inv = (_chave * prox) % mod
        if inv == 1:
            inverso = prox
            break
    return inverso


def blocos_decifra(chave: list, bloco: list):
    _bloco = blocos(bloco)
    c = dict()
    for b in range(0, len(_bloco)):
        c[f"{b}"] = list()
        count = 0
        for i in _bloco[str(b)]:
            cif = (int(i) * chave[count]) % mod
            c[f"{b}"].append(chr(cif))
            count += 1
    return c


if __name__ == '__main__':
    print("=-=-=-=> As chaves informadas devem ser números primos menores que 256 <=-=-=-=")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]
    chave_invMod = [invModular(c) for c in chave]

    cifra = str(input("Informe a cifra separada por espaço: ")).split(" ")
    msg = blocos_decifra(chave_invMod, cifra)

    _msg = str()
    for l in msg:
        for i in msg[l]:
            _msg += i

    print(f"Mensagem: {_msg.replace('-', ' ')}")
