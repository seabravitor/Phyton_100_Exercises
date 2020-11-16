p1 = int(input('Primeiro Termo:'))
raz = int(input('Razão:'))
décimo = p1 + (10 - 1)*raz #para buscar o 10º termo.
for c in range (p1,décimo,raz):
    print('{}'.format(c), end='->')
print('ACABOU')