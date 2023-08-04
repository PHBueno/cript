from table import table

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def key_expand(chave: str, tamanho_msg: int):
    count = 0
    key = list()
    while len(key) < tamanho_msg:
        if count >= len(chave): count = 0
        key.append(chave[count])
        count += 1
    return key


def cifra(chave: int, msg: str):
    key_expanded = key_expand(str(chave), tamanho_msg=len(msg))
    msg_list = list(msg)
    criptograma = str()

    for i in range(len(key_expanded)):

        ################### DECIFRA ###################
        # alfabeto_cif = table[int(key_expanded[i])]  #
        # indice = alfabeto_cif.index(msg_list[i])    #
        # criptograma += alfabeto[indice]             #
        ###############################################

        indice = alfabeto.index(msg_list[i])        # Pega o indice no alfabeto padrão

        alfabeto_cif = table[int(key_expanded[i])]  # Pega o alfabeto de cifragem com base no numero da chave

        criptograma += alfabeto_cif[indice]

    return criptograma


if __name__ == "__main__":
    msg = str(input("Mensagem: ")).upper()
    key = int(input("Informe a Chave: "))

    print(f"Mensagem cifrada: {cifra(chave=key, msg=msg)}")