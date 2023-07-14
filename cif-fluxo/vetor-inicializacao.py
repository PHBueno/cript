##############################################
# Cifras de Fluxo com Vetor de Inicialização #
##############################################

def keystream(vetor_inicial: list, chaves: list):
    count_v = count_c = 0
    fluxo_chaves = list()
    while count_v <= len(vetor_inicial) - 1:
        if count_c >= len(chaves): count_c = 0
        c = (vetor_inicial[count_v] * chaves[count_c])
        fluxo_chaves.append(c)
        count_v += 1
        count_c += 1
    return fluxo_chaves


def cifra(msg: bytes, vetor_inicial: list, chaves: list, arq_saida):
    arquivo = open(arq_saida, 'xb')
    keystreams = keystream(vetor_inicial=vetor_inicial, chaves=chaves)
    k = int()
    for l in msg:
        for n in keystreams:
            k += n
        cif = l ^ (k % 256)
        arquivo.write(cif.to_bytes(1, 'big'))
        keystreams = keystream(vetor_inicial=keystreams, chaves=chaves)
    arquivo.close()


if __name__ == "__main__":
    arquivo_1 = str(input("Informe o arquivo de entrada: "))
    arquivo_2 = str(input("Informe o arquivo de saída: "))

    arq_entrada = open(arquivo_1, 'rb')
    msg = arq_entrada.read()
    arq_entrada.close()

    vi = [(i*21) for i in range(3, 9)]
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 3)]

    cifra(msg=msg, chaves=chave, vetor_inicial=vi, arq_saida=arquivo_2)
