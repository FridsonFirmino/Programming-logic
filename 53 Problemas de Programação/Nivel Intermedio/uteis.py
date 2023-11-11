# FUNÇÃO QUE CONVERTE DE BINARIO PARA DECIMAL
def bin2dec(binNumber):
    valor = 0
    tamanho = len(binNumber) - 1
    for item in binNumber:
        valor += int(item) * 2 ** tamanho
        tamanho = tamanho - 1
    return valor


def reverseString2(st):
    # Esta função também recebe qualquer valor do tipo String e invertea,
    # igual a função reverseString() só que muito mais optimizada
    return st[::-1]
