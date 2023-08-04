def cif(num_msg: list):
    _cif = list()
    for i in num_msg:
        cifragem = (i + 128) % 256
        _cif.append(cifragem)
    return _cif


if __name__ == '__main__':
    msg = str(input('Mensagem: '))
    num_msg = [ord(l) for l in msg]

    cifrado = cif(num_msg=num_msg)
    print(f"Mensagem cifrada: ")
    for i in cifrado:
        print(f'{i}', end=' ')
    print('')
