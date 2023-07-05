##############
# PERMUTAÇÃO #
##############

#########################################################################
# Operação:                                                             #
# - Realizar a operação inversa da cifração O criptograma é escrito por #
# - coluna, definido pela chave, e o texto em claro é lido por linha    #
#########################################################################


def blocos(chave: int, msg: str):
    i = 1
    inicio = _separacao = 0
    bloco = []

    separacao = int(len(msg) / chave)

    while i <= len(msg):
        _separacao += separacao
        bloco.append(msg[inicio:_separacao])
        inicio += separacao
        i += 1
        if inicio >= len(msg):
            break
    return bloco


def decifra(blocos: list, chave: int):
    decifrado = []
    i = 0
    msg = ''.join(blocos)
    separacao = int(len(msg) / chave)
    while i < separacao:
        for c in blocos:
            decifrado.append(c[i])
        i += 1
    msg = ''.join(decifrado)
    return msg.replace("-", " ")


if __name__ == '__main__':
    msg = str(input("Mensagem: "))
    chave = int(input("Chave: "))

    bloco = blocos(chave=chave, msg=msg)
    print(decifra(blocos=bloco, chave=chave))
