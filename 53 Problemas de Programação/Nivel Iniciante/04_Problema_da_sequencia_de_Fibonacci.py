# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 4 - PROBLEMA DA SEQUÊNCIA DE FIBONACCI

A sequência de Fibonacci é construída de forma que cada termo é obtido pela soma dos
dois termos anteriores. Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13.

Programa capaz de solicitar um número inteiro N (1<=N<=40) e informar os N
primeiros elementos (um elemento por linha) da sequência de Fibonacci a partir do zero e
com o segundo elemento 1
"""

N = int(input("Informe um número inteiro no intervalo de 1 á 40: "))

count = 0
n1 = 0
n2 = 1

if (1 <= N <= 40):
    print("Sequência de FIBONACCI: ")
    while count < N:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1
