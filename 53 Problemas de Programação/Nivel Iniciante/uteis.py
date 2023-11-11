# Função que verifica se uma string(Número) está em Hexadecimal
def checkHex(hexaNumber):
    for ch in hexaNumber:
        if ((ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F')):
            continue
        else:
            return False
    return True


def checkLetterLower(ch):
    if (ch >= 'a' and ch <= 'z'):
        return True
    else:
        return False


def reverseString(st):
    # Esta função recebe qualquer valor do tipo String e invertea
    tam = len(st) - 1
    rev = ''
    while tam >= 0:
        rev += st[tam]
        tam -= 1
    return rev


def reverseString2(st):
    # Esta função também recebe qualquer valor do tipo String e invertea,
    # igual a função reverseString() só que muito mais optimizada
    return st[::-1]


def isPrimo(number):
    # Esta função verifica se um número é primo ou não,
    qtdMultiplos = 0
    for x in range(1, number + 1):
        if number % x == 0:
            qtdMultiplos += 1
    if qtdMultiplos == 2:
        return True
    else:
        return False


def getSucessor(number):
    # Esta função recebe um número e returna o seu sucessor
    return number + 1
