N = int(input())
count = 0
listNumber = []

if (1 <= N <= 1000):
    print("")

while count < N:
    n = int(input())
    listNumber.append(n)
    count += 1

for x in list(set(listNumber)):
    print(x)
