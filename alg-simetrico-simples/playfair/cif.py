##################
# CIFRA PLAYFAIR #
##################

# todo: Realizar decifração

caracteres_especiais = ['I', 'J']
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '(I/J)', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Pega somente as primeiras ocorrencias dos caracteres da chave e junta I e J, se houver, formando (I/J)
def trata_chave(key: str) -> list:
    nova_chave = list()
    for letra in key:
        char = letra
        if char in caracteres_especiais: char = '(I/J)'
        if char not in nova_chave:
            nova_chave.append(char.upper())
    return nova_chave


# Remove as letras do alfabeto que já existem na chave.
def trata_alfabeto(key: list) -> list:
    novo_alfabeto = alfabeto.copy()
    for letra in key:
        novo_alfabeto.remove(letra)
    return novo_alfabeto


def matriz(key: str) -> dict:
    chave = trata_chave(key)
    alfabeto = trata_alfabeto(key=chave)
    aux = chave + alfabeto
    m = dict()
    inicio = fim = 0
    for l in range(len(aux)):
        fim += 5
        m[l] = list()
        for letras in aux[inicio:fim]:
            m[l].append(letras)
        inicio += 5
        if inicio >= len(aux): break
    return m


def digrafos(msg: str) -> list:
    count = 0
    digrafo = list()
    while count < len(msg):
        if count+1 < len(msg) and msg[count] == msg[count+1]:  # Se as letras do bloco forem iguais
            digrafo.append(msg[count] + 'X')
            count += 1  # salto único para a próxima letra da mensagem,
            # levando em consideração que a letra 'X' foi adicionada ao bloco e não pertence a mensagem original.

        else:  # Se as letras do bloco não forem iguais
            # Adiciona a letra atual e a próxima ao bloco ( [letra + letra+1] )
            # Se, ao final de todos os blocos, sobrar uma letra sozinha adiciona um caratere 'X' para formar
            # o bloco final.
            digrafo.append(msg[count] + msg[count+1] if count + 1 < len(msg) else msg[count] + 'X')
            count += 2  # Salto duplo para a formação do novo bloco
    return digrafo


def busca_id_linha(matriz: dict, letra: str):
    return [i for i in matriz if letra in matriz[i]]  # retorna o id da linha em que a letra está inserida


def busca_id_coluna(matriz: dict, letra: str):
    pos = int()
    for i in matriz:
        for l in range(len(matriz[i])):
            if letra == matriz[i][l]:
                pos = l
                break
    return pos  # retorna o id da coluna em que a letra está inserida


def cifra(msg: str, key: str):
    contagem_de_digrafos = 0
    d = digrafos(msg)
    m = matriz(key)
    cifra = list()

    while contagem_de_digrafos < len(d):
        contagem_de_rounds = count = 0
        digrafo = list()
        digrafo.append(d[contagem_de_digrafos])

        while count <= len(digrafo):
            letra_round_1 = digrafo[0][0]  # primeira letra do bloco
            letra_round_2 = digrafo[0][1]  # segunda letra do bloco

            rotate = True
            linha = busca_id_linha(matriz=m, letra=letra_round_1)
            coluna = busca_id_coluna(matriz=m, letra=letra_round_2)

            if letra_round_1 in caracteres_especiais:
                letra_round_1 = '(I/J)'
                linha = busca_id_linha(matriz=m, letra=letra_round_1)

            if letra_round_2 in caracteres_especiais:
                letra_round_2 = '(I/J)'
                coluna = busca_id_coluna(matriz=m, letra=letra_round_2)

            bloco_cif = m[linha[0]][coluna]  # Interseção entre linha e coluna do bloco, na matriz.

            # Verifica se ambas as letras estão na mesma linha
            if busca_id_linha(matriz=m, letra=letra_round_1) == busca_id_linha(matriz=m, letra=letra_round_2):
                index_letra_1 = (m[linha[0]].index(letra_round_1) + 1) % 5  # linha circular
                index_letra_2 = (m[linha[0]].index(letra_round_2) + 1) % 5  # linha circular

                letra_cif_1 = m[linha[0]][index_letra_1]
                letra_cif_2 = m[linha[0]][index_letra_2]

                bloco_cif = letra_cif_1 + letra_cif_2
                cifra.append(bloco_cif)
                break  # Para o laço e vai para o próximo bloco

            # Verifica se ambas as letras estão na mesma coluna
            if busca_id_coluna(matriz=m, letra=letra_round_1) == busca_id_coluna(matriz=m, letra=letra_round_2):
                # Tanto faz utilizar a primeira letra ou a segunda, ambas estão na mesma coluna
                index_coluna = busca_id_coluna(matriz=m, letra=letra_round_1)

                # Pula para a próxima linha de forma circular, para ambas as letras do bloco
                index_letra_1 = ((busca_id_linha(matriz=m, letra=letra_round_1)[0]) + 1) % 5
                index_letra_2 = ((busca_id_linha(matriz=m, letra=letra_round_2)[0]) + 1) % 5

                # Pega as letras das próximas linhas, mantendo-se na mesma coluna
                letra_cif_1 = m[index_letra_1][index_coluna]
                letra_cif_2 = m[index_letra_2][index_coluna]

                bloco_cif = letra_cif_1 + letra_cif_2
                cifra.append(bloco_cif)
                break  # Para o laço e vai para o próximo bloco

            cifra.append(bloco_cif)
            count += 1

            # Inverte a ordem do bloco para continuar o processo de cifragem.

            ############
            # exemplo: #
            ############################################################################################################
            # Primeira letra cifrada do bloco: CA => Interseção da linha do caractere 'C' com a coluna do caractere 'A'#
            # Segunda letra cifrada do bloco: AC => Interseção da linha do caractere 'A' com a coluna do caractere 'C' #
            ############################################################################################################

            if rotate:
                if count == len(digrafo):
                    # Se o bloco já foi invertido, para o laço e pula para o próximo bloco
                    if contagem_de_rounds == 1: break

                    digrafo[0] = digrafo[0][::-1]  # Inverte a ordem dos caracteres no bloco => AC = CA
                    count = 0  # retorna a contagem para 0 para iniciar a cifragem do segundo caratere do bloco
                    contagem_de_rounds += 1

        del digrafo  # Limpa o digrafo para receber o bloco seguinte
        contagem_de_digrafos += 1

    return m, cifra


if __name__ == '__main__':
    mensagem = str(input('Informe a mensagem: ')).upper().replace(' ', '')
    chave = str(input('Informe a chave: ')).upper()
    m, criptograma = cifra(msg=mensagem, key=chave)

    print(f'{m}')

    print('-*-*-*-*-*-*-*-MATRIZ-*-*-*-*-*-*-*-')
    for i in m:
        print(m[i])
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    print(criptograma)
