def decif(cifra: list):
    _decif = str()
    for i in cifra:
        decifra = chr((int(i) - 128) % 256)
        _decif += decifra
    return _decif


if __name__ == "__main__":
    cif = str(input("Informe a cifra (somente números separados por espaço): ")).split(" ")

    print(f"Mensagem decifrada: {decif(cifra=cif)}")
