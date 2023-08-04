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
    key = key_expand(str(chave), tamanho_msg=len(msg))
    criptograma = str()

    msg_list = list(msg)

    for i in range(len(key)):
        index_alfabeto = alfabeto.index(msg_list[i])
        cif = (index_alfabeto + int(key[i])) % 26  # decif = (index_alfabeto - int(key[i])) % 26
        criptograma += alfabeto[cif]
    return criptograma


if __name__ == "__main__":
    msg = str(input("Mensagem: ")).upper()
    chave = int(input("Informe um valor numérico para a chave: "))

    print(f"Mensagem cifrada: {cifra(chave=chave, msg=msg)}")

