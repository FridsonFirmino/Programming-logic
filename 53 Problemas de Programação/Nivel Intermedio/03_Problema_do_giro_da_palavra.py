s1 = input("Informe a string S1: ")
s2 = input("Informe a string S2: ")

print('1') if len(s1) == len(s2) and s2 in s1 + s1 else print('0')
