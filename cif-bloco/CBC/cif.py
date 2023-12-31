#########################
# Cipher Block Chaining #
#########################

qnt_bytes_bloco = 8


def bloco_incompleto(qnt_bytes_blc_incompl: int, msg: str):
    blc = {'0': list()}
    _msg = msg
    for i in range(0, qnt_bytes_blc_incompl):
        blc['0'].append(msg[i])
        _msg = msg[i + 1:]
        if i == qnt_bytes_blc_incompl-1:  # Preenche a quantidade incompleta do bloco
            for p in range(i+1, qnt_bytes_bloco):
                blc['0'].append(chr(7))
            break
    return _msg, blc


def bloco(qnt_bytes_blc_incompl: int, msg: str) -> dict:
    _msg = msg
    inicio = fim = count = 0
    blc = {}
    if qnt_bytes_blc_incompl > 0:
        count = 1
        _msg, blc = bloco_incompleto(qnt_bytes_blc_incompl=qnt_bytes_blc_incompl, msg=msg)
    while count <= len(_msg):
        blc[f'{count}'] = list()
        fim += 8
        for letra in _msg[inicio:fim]:
            blc[f'{count}'].append(letra)
        inicio += 8
        count += 1
        if inicio >= len(_msg): break
    return blc


def cifra(chave: list, vetor_inicial: list, msg: str, qnt_bytes_blc_incompl: int) -> dict:
    blocos_cif = {}
    blocos = bloco(msg=msg, qnt_bytes_blc_incompl=qnt_bytes_blc_incompl)
    for b in blocos:
        blocos_cif[b] = list()
        # print(f"BLOCO: {b}")
        for i in range(0, len(blocos[str(b)])):
            # print(f"  -> {ord(blocos[str(b)][i])} XOR {vetor_inicial[i]}")
            xor = ord(blocos[str(b)][i]) ^ vetor_inicial[i]  # Realiza XOR com o Vetor
            cif = (xor * chave[i]) % 256 # Cifragem
            blocos_cif[b].append(cif)
        vetor_inicial = [l for l in blocos_cif[b]]  # Vetor Inicial recebe o bloco cifrado anteriormente
    return blocos_cif


def apresenta(cifra: dict) -> str:
    out = str()
    for b in cifra:
        for l in cifra[b]:
            out += l
    return out


if __name__ == "__main__":
    vetor_inicial = [x+20 for x in range(0, qnt_bytes_bloco)]

    msg = str(input("Mensagem a ser cifrada: "))
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]

    tamanho = len(msg)
    qnt_bytes_blc_incompl = tamanho % 8

    cifragem = cifra(chave, vetor_inicial, msg, qnt_bytes_blc_incompl)

    for b in cifragem:
        for l in cifragem[b]:
            print(f'{l}', end=' ')
    print('\n')
