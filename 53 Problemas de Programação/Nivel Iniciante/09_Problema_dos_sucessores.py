# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 9 - PROBLEMA DOS SUCESSORES

Faça um programa que solicite números inteiros I (-4000<=I<=4000) enquanto I for
diferente de zero. Quando I for zero o programa deve imprimir todos os sucessores
inteiros imediatos de cada I informado.

Observe que neste problema não há um limite para a quantidade de números I
informados.
"""
import uteis

count = 1
numberList = []
while count != 0:
    i = int(input("Informe um número: "))
    numberList.append(i)
    count = i

numberList.pop()
print("")
for x in numberList:
    print("O sucessor de ", x, " é ", uteis.getSucessor(x))
