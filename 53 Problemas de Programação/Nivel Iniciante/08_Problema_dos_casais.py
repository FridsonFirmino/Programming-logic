# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 8 - PROBLEMA DOS CASAIS

Em um bar, os homens recebem cartão de identificação com números ímpares e as
mulheres cartões com números pares.

Um animador contratado para animar a programação do dia deseja saber se existe uma
proporção de um-para-um entre homens e mulheres.

O programa receberá um número N (1<=N<=1000) com o número de cartões distribuídos
e uma lista com N números inteiros positivos (todos maior ou igual a 1 e menor ou igual a
500) cada um representando o número de um cartão. A saída deverá ser uma única linha
com o caractere S caso exista a proporção ou com o caractere N caso contrário.
"""

N = int(input("Informe a quantidade de Cartões: "))

listCart = []
count = 0
qtdImpar = 0
qtdPar = 0

while count < N:
    num = int(input())
    if (num >= 1 and num <= 500):
        listCart.append(num)
    count += 1

print(listCart)
for x in listCart:
    if x % 2 == 0:
        qtdPar += 1
    else:
        qtdImpar += 1

print("S") if qtdPar == qtdImpar else print("N")
