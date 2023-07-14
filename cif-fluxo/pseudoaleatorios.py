###############################################
# Cifra de Fluxo com Valores Pseudoaleatórios #
###############################################


def cifra(msg: bytes, chave: list, arq_saida):
    arq = open(arq_saida, 'xb')
    for i in msg:
        chave[0] = (63 * chave[0] + 97) % 249
        chave[1] = (59 * chave[1] + 47) % 239
        chave[2] = (21 * chave[2] + 61) % 200

        keystream = (chave[0] + chave[1] + chave[2]) % 256  # Geração do Keystream para cada byte da mensagem;
        arq.write((keystream ^ i).to_bytes(1, 'big'))  # Realiza a combinação da Keystream com o byte do testo em claro
    arq.close()


if __name__ == "__main__":
    arquivo1 = str(input("Informe o arquivo a ser cifrado: "))
    arquivo2 = str(input("Informe o arquivo de saída: "))

    print("\nInforme três valores inteiros numéricos para compor a chave:")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 3)]

    arq_entrada = open(arquivo1, 'rb')
    msg = arq_entrada.read()
    arq_entrada.close()

    cifra(msg=msg, chave=chave, arq_saida=arquivo2)
    print(f"\nProcessamento finalizado! Arquivo cifrado: {arquivo2}")
