# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
#3 - Problema do número espelho

Programa que recebendo um número inteiro positivo N em hexadecimal seja
capaz de verificar se este número em decimal é lido exatamente da mesma forma seja de
frente para trás ou de trás para frente.

Caso positivo o programa deverá retornar uma linha com o caractere S, caso contrário o
caractere informado deverá ser o N
"""
import uteis
n = input("Informe um número em HEXADECIMAL: ")
if uteis.checkHex(n):
    numDececimal = int(n, 16)
    numDececimalInvertido = int(uteis.reverseString2(str(numDececimal)))
    print("S") if numDececimal == numDececimalInvertido else print("N")
else:
    print("O número não está em HEXADECIMAL")
