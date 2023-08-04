import string

alfabeto = list(string.ascii_uppercase)


def key_expand(chave: str, tamanho_msg: int) -> list:
    count = 0
    key = list()
    while len(key) < tamanho_msg:
        if count >= len(chave): count = 0
        key.append(chave[count])
        count += 1
    return key


def cif(chave: str, msg: str):
    key = key_expand(chave=chave, tamanho_msg=len(msg))
    _msg = list(msg)
    _cif = list()

    for i in range(len(_msg)):
        rotacao = alfabeto.index(key[i])
        atual = alfabeto.index(_msg[i])
        # decifra = (atual - rotacao) % 26
        cifra = (atual + rotacao) % 26  # Realiza a rotação para voltar para a inicial do alfabeto caso a soma dê
                                        # número maior que o tamanho do alfabeto
        _cif.append(alfabeto[cifra])
    return _cif


if __name__ == '__main__':
    msg = str(input("Informe a mensagem: ")).upper().replace(' ', '')
    chave = str(input("Informe a chave: ")).upper()
    cifra = cif(chave=chave, msg=msg)

    print(cifra)
