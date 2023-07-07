###########################################################################
# Operação => Substituição Polialfabética:                                #
# - A primeira ocorrência do caractere é substituída pelo alfabeto_subs_1 #
# - A segunda ocorrência do caractere é substituída pelo alfabeto_subs_2  #
# - A terceira ocorrência do caractere não é substuída                    #
# - A quarta ocorrência do caractere é substituída pelo alfabeto_subs_1   #
# - Assim por diânte                                                      #
###########################################################################

import pyfiglet

banner = pyfiglet.figlet_format("Polialfabetica", format('doom'))

# Alfabetos de substituições
alfabeto        = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
alfabeto_subs_1 = "ERT-DVBXWLAKZINQCFGHMOPSUYJ"
alfabeto_subs_2 = "DTWEVBMRL-UINXYCFGHJQSKZOPA"


# Cria relação entre o alfabeto e as tabelas de substituições
def tabela_subs(alfabeto_subs: str, alfabeto_originario: str):
    subs_schema = {}
    for i in range(0, len(alfabeto_originario)):
        subs_schema[alfabeto_originario[i]] = alfabeto_subs[i]
    return subs_schema


# Armazena em um dicionário a quantidade de ocorrências de cada letra e
# as posições, na palavra, que as letras repetidas estão.
def ocorrencias(msg: str):
    oc = {}
    pos = 0
    l = 0
    _index = []
    for i in range(0, len(msg)):
        while l < len(alfabeto):
            index = msg.find(alfabeto[l], pos)
            if index == -1:  # Não encontrou a letra na mensagem
                _index = []
                l += 1
                pos = 0
                pass
            else:  # Encontrou a letra na mensagem
                _index.append(index)
                oc[f"{alfabeto[l]}"] = _index
                pos = index + 1
        l = 0
        pos = 0
    return oc


# Realiza as substituições com base na regra estabelecida para criptografar
def cif(msg: str):
    oc = ocorrencias(msg)
    _msg = msg
    s1 = tabela_subs(alfabeto_subs=alfabeto_subs_1, alfabeto_originario=alfabeto)
    s2 = tabela_subs(alfabeto_subs=alfabeto_subs_2, alfabeto_originario=alfabeto)
    for l in oc:
        cont = 0
        quantidade = oc[l]
        while True:
            if cont >= len(quantidade):
                break
            if cont == 0:
                _msg = _msg[:quantidade[0]] + s1[l] + _msg[quantidade[0] + 1:]
            if len(quantidade) >= 2:
                _msg = _msg[:quantidade[1]] + s2[l] + _msg[quantidade[1] + 1:]
                del quantidade[0:2]
                cont = 0
                if len(quantidade) >= 1:
                    _msg = _msg[:quantidade[0]] + l + _msg[quantidade[0] + 1:]
                    del quantidade[0]
            else:
                cont += 1
    return _msg


def dcif(msg: str):
    oc = ocorrencias(msg)
    _msg = msg
    s1 = tabela_subs(alfabeto_subs=alfabeto, alfabeto_originario=alfabeto_subs_1)
    s2 = tabela_subs(alfabeto_subs=alfabeto, alfabeto_originario=alfabeto_subs_2)
    for l in oc:
        cont = 0
        quantidade = oc[l]
        while True:
            if cont >= len(quantidade):
                break
            if cont == 0:
                _msg = _msg[:quantidade[0]] + s1[l] + _msg[quantidade[0] + 1:]
            if len(quantidade) >= 2:
                _msg = _msg[:quantidade[1]] + s2[l] + _msg[quantidade[1] + 1:]
                del quantidade[0:2]
                cont = 0
                if len(quantidade) >= 1:
                    _msg = _msg[:quantidade[0]] + l + _msg[quantidade[0] + 1:]
                    del quantidade[0]
            else:
                cont += 1
    return _msg


if __name__ == '__main__':
    print(banner)
    escolha = int(input("Escolha [1 - Cifrar; 2 - Decifrar]: "))
    msg = str(input("Mensagem: ")).upper()
    msg = msg.replace(" ", "-")

    if escolha == 1:
        print('-=' * len(msg))
        print(f"Cifra: {cif(msg=msg)}")
        print('-=' * len(msg))
    elif escolha == 2:
        print('-=' * len(msg))
        print(ocorrencias(msg))
        print(f"Decifra: {dcif(msg=msg)}")
        print('-=' * len(msg))
