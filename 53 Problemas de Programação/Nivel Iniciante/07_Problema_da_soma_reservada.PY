# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 7 - PROBLEMA DA SOMA RESERVADA

Para este problema considere que a soma reservada de N + M é dada por Rev(Rev(N) +
Rev(M)), sendo que Rev(X) é uma função que retorna X com os algarismos na ordem
inversa. Por exemplo, Rev(5789) = 9875.

Faça um programa capaz de receber dois números inteiros e informar a soma reservada
do mesmo.
"""
import uteis

N = input("Informe um número: ")
M = input("Informe outro número: ")

resultado = uteis.reverseString2(
    str(int(uteis.reverseString2(N)) + int(uteis.reverseString2(M))))
print(resultado)
