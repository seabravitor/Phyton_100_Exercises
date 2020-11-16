r1 = int(input('Tamanho reta 1: '))
r2 = int(input('Tamanho reta 2: '))
r3 = int(input('Tamanho reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('As retas formam um triângulo:', end=' ')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('As retas não formam um triângulo')