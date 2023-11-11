# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
#2 - PROBLEMA DA MÉDIA

Programa capaz de solicitar um número inteiro N (1<N<1000) do usuário e ler N
números inteiros. Ao final da leitura do último número, o programa deverá informar, com
uma casa decimal, a média aritmética entre os N números que estejam contidos no
intervalo fechado entre -1000 e 1000.
"""

N = int(input("Informe um número: "))

count = 0
valoresDados = 0
qtdDados = 0
if (1 < N < 1000):
    while count < N:
        n = int(input("Informe o número: "))
        if ((n > -1000) and (n < 1000)):
            valoresDados += n
            qtdDados += 1
        count += 1
    print(valoresDados / qtdDados)
