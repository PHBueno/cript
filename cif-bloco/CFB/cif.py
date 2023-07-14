#########################
# Cipher Feedback Block #
#########################

##########################################################################################
# Inicia-se o processo com um vetor de inicialização;                                    #
# O Vetor de Inicialização é cifrado através do processo de cifração => Vetor cifrado;   #
# O Vetor Cifrado é combinado (XOR) com o texto em claro => Bloco Cifrado;               #

# ========================== Repetição até o final dos blocos ==============   ###########
# O Bloco Cifrado passa pelo processo de cifração e é combinado (XOR)
# com o próximo bloco de texto em claro => realimentação


qntd_bytes_bloco = 8


def bloco_incompleto(qntd_byte_bloco_incompl: int, msg: str):
    blc = {'0': list()}
    _msg = msg
    for i in range(0, qntd_byte_bloco_incompl):
        blc['0'].append(msg[i])
        _msg = msg[i + 1:]
        if i == qntd_byte_bloco_incompl-1:  # Preenche a quantidade incompleta do bloco
            for p in range(i + 1, qntd_bytes_bloco):
                blc['0'].append(chr(7))
            break
    return _msg, blc


def bloco(qntd_byte_bloco_incompl: int, msg: str):
    _msg = msg
    inicio = fim = count = 0
    blc = {}
    if qntd_byte_bloco_incompl > 0:  # Existe bloco incompleto
        count = 1  # Próximo bloco (O 0 é o bloco incompleto)
        _msg, blc = bloco_incompleto(qntd_byte_bloco_incompl=qntd_byte_bloco_incompl, msg=msg)
    while count <= len(_msg):
        blc[f'{count}'] = list()
        fim += 8
        for letra in _msg[inicio:fim]:
            blc[f'{count}'].append(letra)
        inicio += 8
        count += 1
        if inicio >= len(_msg): break
    return blc


def cifra(vi: list, chave: list, msg: str, qntd_byte_bloco_incompl: int):
    blocos = bloco(qntd_byte_bloco_incompl=qntd_byte_bloco_incompl, msg=msg)
    for b in blocos:
        proximo_xor = [((vi[i] * chave[i]) % 256) for i in range(0, len(vi))]  # A cifragem é realizada no VI
        cifragem = [ord(blocos[b][i]) ^ proximo_xor[i] for i in range(0, len(blocos[b]))]  # Realiza XOR com o Bloco
        vi = cifragem  # O vetor de inicialização é substituído pelo valor do bloco cifrado
        blocos[b] = cifragem
    return blocos


if __name__ == "__main__":
    msg = str(input("Informe a mensagem: "))
    vetor_inicial = [i+20 for i in range(0, qntd_bytes_bloco)]
    print("\nEntre com a chave: 8 valores menores que 256.\n")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, qntd_bytes_bloco)]

    tamanho = len(msg)
    qntd_bytes_bloco_imcompl = tamanho % 8

    cifragem = cifra(vi=vetor_inicial, chave=chave, qntd_byte_bloco_incompl=qntd_bytes_bloco_imcompl, msg=msg)

    print("\nMensagem cifrada: ", end=' ')
    for b in cifragem:
        for l in cifragem[b]:
            print(f'{l}', end=' ')
    print('\n')
