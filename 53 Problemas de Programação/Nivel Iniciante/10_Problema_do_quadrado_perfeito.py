# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 10 - PROBLEMA DO QUADRADO PERFEITO

Um número inteiro positivo N é um quadrado perfeito se existe um número K tal que
K*K=N.

Faça um programa que receberá uma quantidade indefinida de números inteiros positivos
J (-10000<=J<=10000) até que J seja zero. A saída do programa deverá ser a quantidade
de quadrados perfeitos informados.
"""

count = 1
qtdQuadradoPerfeito = 0
numberList = []
while count != 0:
    i = int(input("Informe um número: "))
    numberList.append(i)
    count = i

numberList.pop()
print("")
for x in numberList:
    for i in range(x):
        if i * i == x:
            qtdQuadradoPerfeito += 1

print(qtdQuadradoPerfeito)
