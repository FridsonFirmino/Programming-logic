# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 6 - PROBLEMA DO QUADRADO GÊMEO DAS PARTES

Existem alguns números que têm uma propriedade bastante interessante, observe:

    EXEMPLO: 100
                10+0=10 10*10=100
    EXEMPLO: 2025
                20+25=45 45*45=2025
    EXEMPLO: 3025
                30+25=55 55*55=3025

Os números que têm esta propriedade são conhecidos como número de Kaprekar.
Cada um dos números apresentados tiveram seus algarismos decompostos de tal forma
que a soma das partes elevado ao quadrado era igual ao número original.

Faça um programa capaz de ler e identificar se um determinado número N
(1<=N<=100.000.000) possui ou não esta propriedade. Caso positivo, o programa deverá
retornar uma única linha com o valor 1, caso contrário deve-se retornar uma linha com
valor 0.
"""

n = input("Informe um número: ")
tam = len(n)
if tam % 2 == 0:
    indice = int(tam/2)
    algarismo1 = int(n[:indice])
    algarismo2 = int(n[indice:])
    KaprekarNumber = (algarismo1 + algarismo2) ** 2
    print("1") if (KaprekarNumber == int(n)) else print("0")
else:
    indice = int(tam/2)
    algarismo1 = int(n[:indice+1])
    algarismo2 = int(n[indice+1:])
    KaprekarNumber = (algarismo1 + algarismo2) ** 2
    print("1") if (KaprekarNumber == int(n)) else print("0")
