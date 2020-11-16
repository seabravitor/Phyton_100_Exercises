print ('{:=^40}'.format('Gerador de P.A'))
n = int(input('Digite o primeiro termo: '))
r = int(input('Razão da P.A: '))
termo = n
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    c = c + 1
print('FIM')



