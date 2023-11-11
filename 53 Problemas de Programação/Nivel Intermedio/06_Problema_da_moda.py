count = 1
listNumber = []
dic = {}
newDic = {}
while count != 0:
    n = int(input())
    listNumber.append(n)
    count = n

print("\n")
for x in listNumber:
    dic[x] = listNumber.count(x)

maior = max(dic, key=dic.get)
for x in dic:
    if dic[maior] <= dic[x]:
        newDic[x] = dic[x]

for x in sorted(list(newDic)):
    print(x)
