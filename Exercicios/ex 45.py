from time import sleep
from random import randint
print('{:=^40}'.format(' JOKENPÔ '))
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
print('='*40)
lista = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)
jogada = int(input('Escolha a sua jogada: '))
print('='*40)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('='*40)
print ('''Você escolheu: {}
O computador escolheu: {}'''.format(lista[jogada],lista[comp]))
if comp == 0:
    if jogada == 0:
        print('O resultado é: EMPATE')
    elif jogada == 1:
        print('O resultado é: VITÓRIA HUMANA')
    elif jogada == 2:
        print('O resultado é: VITÓRIA COMPUTADOR')
elif comp == 1:
    if jogada == 0:
        print('O resultado é: VITÓRIA COMPUTADOR')
    elif jogada == 1:
        print('O resultado é: EMPATE')
    elif jogada == 2:
        print('O resultado é: VITÓRIA HUMANA')
elif comp == 2:
    if jogada == 0:
        print('O resultado é: VITÓRIA HUMANA')
    if jogada == 1:
        print('O resultado é: VITÓRIA COMPUTADOR')
    if jogada == 2:
        print('O resultado é: EMPATE')