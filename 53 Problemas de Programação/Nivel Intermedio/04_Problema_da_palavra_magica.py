p = input("")
tam = len(p)
if ((2 <= tam <= 100) and (tam % 2 != 0)):
    print("N")
else:
    print("S") if sorted(p[:int(tam/2)]
                         ) == list(p[int(tam/2):]) else print("N")
