##############
# PERMUTAÇÃO #
##############

###############################################################################
# Operação => Permutação:                                                     #
# - Realizar a escrita por linhas e obter o texto cifrado lendo as colunas.   #
# - A quantidade de colunas é definida pela chave especificada                #
###############################################################################


def blocos(chave: int, msg: str):
    i = 1
    nova_msg = []
    _chave = 0
    inicio = 0
    while i <= len(msg):
        _chave += chave
        nova_msg.append(msg[inicio:_chave])
        inicio += chave
        i += 1
        if inicio >= len(msg):  # Chegou ao final do texto original
            if len(nova_msg[-1]) < chave:
                dif = chave - len(nova_msg[-1])
                nova_msg[-1] += ("X" * dif)
            break
    return nova_msg


def cifra(chave: int, msg: str):
    _cifra = blocos(chave=chave, msg=msg)
    cifrado = []
    i = 0
    while i < chave:
        for c in _cifra:
            cifrado.append(c[i])
        i += 1
    return ''.join(cifrado)


if __name__ == '__main__':
    msg = str(input("Mensagem: "))
    chave = int(input("Chave: "))
    msg = msg.replace(" ", "-").upper()
    print(cifra(chave=chave, msg=msg))
