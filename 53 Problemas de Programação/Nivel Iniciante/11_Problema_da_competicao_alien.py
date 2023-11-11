# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
# 11 - PROBLEMA DA COMPETIÇÃO ALIEN

Os aliens do planeta Yks fazem uma competição para ver quem consegue escreve um
texto com o maior número de palavras com N (1<=N<=10) caracteres.

Faça um programa para automatizar o cálculo e contar quantas palavras com N
caracteres existem no texto digitado. O programa deverá receber o número N e um texto
com até 250 caracteres e deverá dar como saída a quantidade de palavras com N sílabas
que o texto contém.

Atenção: para resolver este problema você necessita saber que na escrita do povo de
Yks não é utilizado espaço nem mesmo para separar palavras, ao invés disto, qualquer
caractere que não seja uma letra minúscula entre a e z será considerado separador de
palavra.
"""
import uteis

N = int(input("Informe um número: "))
frase = input("informe a frase: ")

palavra = ''
palavrasList = []
qtdPalavra = 0

for x in frase + '0':
    if uteis.checkLetterLower(x):
        palavra += x
    else:
        if len(palavra) == N:
            qtdPalavra += 1
        palavra = ''

print(qtdPalavra)
