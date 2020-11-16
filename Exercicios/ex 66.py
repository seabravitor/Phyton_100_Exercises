print(' {:~^40} '.format(' ex 66 - Números com Flag '))
n = 0
qtd = 0
termo = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    termo = termo + n
    qtd = qtd + 1
    n = int(input('Digite um valor [999 para parar]: '))
print('A soma dos {} valores é de: {}'.format(qtd,termo))