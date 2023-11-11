import uteis

operacao = input("Informe a operação(+,-,*,/,%): ")
if operacao == '+':
    numB = input("Informe um numero em binario: ")
    numB2 = input("Informe outro numero em binario: ")
    resultado = bin((uteis.bin2dec(numB)) +
                    (uteis.bin2dec(numB2))).lstrip("0b")
    while len(str(resultado)) < 8:
        resultado = '0' + resultado
    print(resultado)
elif operacao == '-':
    numB = input("Informe um numero em binario: ")
    numB2 = input("Informe outro numero em binario: ")
    resultado = bin((uteis.bin2dec(numB)) -
                    (uteis.bin2dec(numB2))).lstrip("0b")
    while len(str(resultado)) < 8:
        resultado = '0' + resultado
    print(resultado)
elif operacao == '*':
    numB = input("Informe um numero em binario: ")
    numB2 = input("Informe outro numero em binario: ")
    resultado = bin((uteis.bin2dec(numB)) *
                    (uteis.bin2dec(numB2))).lstrip("0b")
    while len(str(resultado)) < 8:
        resultado = '0' + resultado
    print(resultado)
elif operacao == '/':
    numB = input("Informe um numero em binario: ")
    numB2 = input("Informe outro numero em binario: ")
    resultado = bin((uteis.bin2dec(numB)) /
                    (uteis.bin2dec(numB2))).lstrip("0b")
    while len(str(resultado)) < 8:
        resultado = '0' + resultado
    print(resultado)
elif operacao == '%':
    numB = input("Informe um numero em binario: ")
    numB2 = input("Informe outro numero em binario: ")
    resultado = bin((uteis.bin2dec(numB)) %
                    (uteis.bin2dec(numB2))).lstrip("0b")
    while len(str(resultado)) < 8:
        resultado = '0' + resultado
    print(resultado)
else:
    print("Operação Inválida")
