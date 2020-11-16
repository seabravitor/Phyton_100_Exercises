from time import sleep
print('='*40)
print('{: ^40}'.format('BANCO BRADESCO'))
print('='*40)
saque = int(input('Que valor gostaria de sacar? R$'))
total = saque
céd = 50
qtd = 0
print('{: ^40}'.format('$...IMPRIMINDO...$'))
sleep(0.5)
while True:
    if total >= céd:
        total = total - céd
        qtd = qtd + 1
    else:
        if qtd > 0:
            print(f'{qtd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        qtd = 0
        if qtd == 0:
            break
print('Use com sabedoria')