caracteres = 8  # quantidade de caracteres por bloco = blocos de 64 bits
mod = 256


def bloco(msg: str) -> list:  # Separa os caracteres em blocos de 64 bits
    i = 1
    blocos = []
    _chave = 0  # Variável de controle para saber até que posição copiar o dado
    inicio = 0  # Variável de controle para saber em que posição começar a copiar o dado
    while i <= len(msg):
        _chave += caracteres
        blocos.append(msg[inicio:_chave])
        inicio += caracteres
        i += 1
        if inicio >= len(msg):  # Chegou ao final do texto original
            if len(blocos[-1]) < caracteres:
                dif = caracteres - len(blocos[-1])
                blocos[-1] += ("X" * dif)
            break
    return blocos


def ascii(blocos: list) -> dict:  # Transforma os caracteres em seus respectivos códigos ASCII
    m = dict()
    for i in range(0, len(blocos)):
        m[f"{i}"] = []
        for l in blocos[i]:
            m[f"{i}"].append(ord(l))
    return m


def blocos_cifra(chave: list, bloco: list) -> dict:  # Cifra os dados em blocos de 64 bits
    _ascii = ascii(bloco)
    c = dict()
    for b in range(0, len(_ascii)):
        c[f"{b}"] = list()
        count = 0
        for i in _ascii[str(b)]:
            cif = (i * chave[count]) % mod  # Cifragem
            c[f"{b}"].append(cif)
            count += 1
    return c


if __name__ == '__main__':
    print("=-=-=-=> As chaves informadas devem ser números primos menores que 256 <=-=-=-=")
    chave = [int(input(f"Ch[{i}]: ")) for i in range(0, 8)]
    msg = str(input("\nMensagem a ser cifrada: ")).lower().replace(' ', '-')
    cifra = blocos_cifra(chave=chave, bloco=bloco(msg))
    print(f"Bloco: {bloco(msg)}")

    print("\n-=" * len(cifra))
    print("Mensagem cifrada: ")
    for l in cifra:
        for i in cifra[l]:
            print(f'{i}', end=' ')
    print("-=" * len(cifra))




