# AUTOR: FRIDSON FIRMINO
# GitHUB: fridsonfirmino
# LINKEDIN: Fridson Firmino

"""
#5 - PROBLEMA DA CONJECTURA DE GOLDBACH

A conjectura de Goldbach (ainda não provada) diz que qualquer número par maior ou
igual a 4 é a soma de dois números primos.

Programa que, recebendo um número P par (2<=P<=4294967294), seja capaz
de retornar dois número inteiros correspondentes aos dois números primos cuja soma
seja igual ao número par P.

Considere que:

    * Os valores de saída devem ser ordenados em ordem crescente.
        Existindo mais de uma combinação possível, retorna-se aquela cujo primeiro valor
        seja o menor.
    * Não existindo valores (parabéns! você foi o primeiro no mundo que provou que a
        conjectura é falsa!) retorne -1.
    * Lembre-se: número primo é todo número inteiro maior que 1 que somente é divisível por
        si próprio e pela unidade.
"""
import uteis

P = int(input("Informe um número: "))
numPrimo1 = 0
numPrimo2 = 0

if (2 <= P <= 4294967294):
    for x in range(2, P+1):
        if uteis.isPrimo(x):
            numPrimo1 = x
            for i in range(x+1, P+1):
                if uteis.isPrimo(i):
                    numPrimo2 = i
                    if (numPrimo1 + numPrimo2) == P:
                        break
                    else:
                        continue
            if (numPrimo1 + numPrimo2) == P:
                break

    print(numPrimo1)
    print(numPrimo2)
