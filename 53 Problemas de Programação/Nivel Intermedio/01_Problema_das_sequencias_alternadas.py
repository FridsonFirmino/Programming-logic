"""
# 1 - Problema das sequências alternadas

Faça um programa que
    1. Leia um número N.
    2. Leia N seqüências de 5 números inteiros.
    3. Imprima as N seqüências alternando a ordem de crescente para decrescente.

Se desejar pode-se assumir que o N máximo será 1000.
A entrada e a saída devem ser conforme o exemplo abaixo.



N = int(input("Informe um número: "))

count1 = 1
count2 = 1
sequencias = []
listSequencias = []
countAux = 1

while count1 <= N:
    print("\n" + str(count1) + "º SEQUENCIA")
    print("================================")
    while count2 <= 5:
        n = int(input(str(count2) + "º número da " +
                str(count1) + "º sequencia: "))
        sequencias.append(n)
        count2 += 1
    count2 = 1
    listSequencias.append(sequencias)
    sequencias = []
    count1 += 1


for x in listSequencias:
    if countAux % 2 != 0:
        print(sorted(x))
    else:
        print(sorted(x, reverse=True))
    countAux += 1
"""

# =============================================================
# ======================== VIRIACÃO 1 =========================
# =============================================================
"""
# Variação 1

Resolva o mesmo problema só que assuma que o número de elementos em cada
seqüência pode variar.

    •Antes de cada sequência o usuário informá qual o número de elementos da
    sequência.

N = int(input("Informe um número: "))

count1 = 1
count2 = 1
sequencias = []
listSequencias = []
countAux = 1

while count1 <= N:
    print("\n" + str(count1) + "º SEQUENCIA")
    print("================================\n")
    qtdN = int(input("Informe aquantidade de números da " +
               str(count1) + "º sequencia: "))
    while count2 <= qtdN:
        n = int(input(str(count2) + "º número da " +
                str(count1) + "º sequencia: "))
        sequencias.append(n)
        count2 += 1
    count2 = 1
    listSequencias.append(sequencias)
    sequencias = []
    count1 += 1

for x in listSequencias:
    if countAux % 2 != 0:
        print(sorted(x))
    else:
        print(sorted(x, reverse=True))
    countAux += 1
"""
