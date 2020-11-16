total = cont = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont = cont + 1
    total = total + num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = total / cont
print('Entre os {} números digitados, o total é de {} com média {:.1f}.'.format(cont,total,media))
print('O maior número foi o {} e o menor {}'.format(maior,menor))