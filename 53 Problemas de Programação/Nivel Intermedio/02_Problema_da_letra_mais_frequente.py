"""
# 2 - Problema da letra mais frequente

Faça um programa capaz de identificar a(s) letra(s) mais frequente(s) em uma cadeia de
caracteres.

A entrada será uma cadeia de caracteres sem espaços de no máximo 1000 caracteres. A
saída deverá ser a(s) letra(s) mais frequente(s) seguida por sua porcentagem com duas
casas decimais.

Deve-se desconsiderar diferenças de maiúsculas e minúsculas.
Qualquer outro caractere que não seja uma letra de A a Z deverá ser desconsiderado no
cálculo da porcentagem e na contagem. A saída deve ser dada em letras minúsculas.
"""
chs = input("")
dic = {}
tam = 0
newDic = {}
for x in chs:
    if x.isalpha():
        dic[x] = chs.count(x)
        tam += 1

maior = max(dic, key=dic.get)
for x in dic:
    if dic[maior] <= dic[x]:
        newDic[x] = dic[x]

for x in newDic:
    resultado = f'{x} {((newDic[x]/tam)*100):.2f}%'
    print(resultado)
