# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 1 - PROBLEMA DA SOMA

Programa capaz de solicitar um número N (1<N<1000) do usuário e ler N
números inteiros. Após a leitura do último número deve-se informar:

    * Na primeira linha a soma dos N números em decimal.
    * Na segunda linha a soma em hexadecimal dos números pares informados.
    * Na terceira linha a soma em octal dos números impares informados.
"""

N = int(input("Informe um número: "))

count = 1
somaNnumerosDec = 0
somaNnumerosParesHexa = 0
somaNnumerosImparesOctal = 0

if (1 < N < 1000):
    while count <= N:
        n = int(input("Informe um número: "))
        somaNnumerosDec += n
        if (n % 2 == 0):
            somaNnumerosParesHexa += n
        else:
            somaNnumerosImparesOctal += n
        count += 1

    print(somaNnumerosDec)
    print(hex(somaNnumerosParesHexa).lstrip("0x"))
    print(oct(somaNnumerosImparesOctal).lstrip("0o"))
