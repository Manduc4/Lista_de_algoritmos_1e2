n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2:
    if n2 > n3:
        print(n1,' ',n2,' ',n3)
    else:
        if n1 > n3:
            print(n1,' ',n3,' ',n2)
        else:
            print(n3, ' ', n1, ' ', n2)
else:
    if n1 > n3:
        print(n2,' ',n1,' ',n3)
    else:
        if n3 > n2:
            print(n3, ' ', n2, ' ', n1)
        else:
            print(n2, ' ', n3, ' ', n1)








