import os


def bloco_incompleto(qntd_bits_bloco_incompl: int, msg: str, arq_out, chave: list):
    aux = list()
    _msg = msg
    preenche = 8 - qntd_bits_bloco_incompl
    for i in range(0, qntd_bits_bloco_incompl):
        aux.append(chr(ord(msg[i]) * chave[i]))  # Cifragem
        _msg = msg[i+1:]
        if i == qntd_bits_bloco_incompl-1:  # Final do bloco incompleto
            aux[-1] += (chr(7) * preenche)  # Preenche com caractere BELL
    with open(arq_out, 'x') as file:
        for i in aux:
            file.write(i)  # Escreve no arquivo de saída
    return _msg


def blocos(msg: str, qntd_bits_bloco_incompl: int, arq_out, chave: list) -> list:
    blocos = list()
    i = 1
    fim = inicio = 0
    _msg = msg
    if qntd_bits_bloco_incompl > 0:
        _msg = bloco_incompleto(qntd_bits_bloco_incompl, msg, arq_out, chave)
    while i <= len(_msg):
        fim += 8
        blocos.append(_msg[inicio:fim])
        inicio += 8
        i += 1
        if inicio >= len(_msg): break
    return blocos


def cifragem(arq_out, msg: str, qnt_bits_bloco_icompl: int, chave: list):
    bloco = blocos(msg=msg,
                   qntd_bits_bloco_incompl=qnt_bits_bloco_icompl,
                   arq_out=arq_out, chave=chave)

    with open(arq_out, 'a') as file:
        for b in bloco:
            count = 0
            for ltr in b:
                cif = (chr(ord(ltr) * chave[count]))
                file.write(cif)
                count += 1


if __name__ == '__main__':
    arq_entrada = str(input("Arquivo de entrada: "))
    arq_saida = str(input("Arquivo de saída: "))

    print('\n')
    print("=-" * 9)
    print("Informe valores ímpares para as chaves\n")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]
    print("=-" * 9)

    arq_1 = open(arq_entrada, "r")
    msg = arq_1.read().replace('\n', '$').replace(' ', '-')
    arq_1.close()

    # Variáveis para controle de tamanhos
    tamanho = os.stat(arq_entrada).st_size  # Tamanho, em bits, do arquivo
    qntd_blocos = int(tamanho / 8)
    qntd_bits_bloco_incompl = tamanho % 8  # Quantidade de bits do bloco incompleto

    cifragem(arq_out=arq_saida,
             qnt_bits_bloco_icompl=qntd_bits_bloco_incompl,
             msg=msg,
             chave=chave)

    print("\n!! Processamento finalizado !!")


