num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Binário - Apenas 2 números - 0,1;
[ 2 ] Octal - com 8 números - de 0 à 7;
[ 3 ] Hexadecimal - com 16 números - de 0 à 9 + A B C D E F''')
conv = int(input('Sua opção é: '))
if conv == 1:
    print('{} convertido em Binário, é: {}.'.format(num, bin(num))
elif conv == 2:
    print('{} convertido para Octal, é: {}'.format(num, oct(num)))
elif conv == 3:
    print('{} convertido para Hexadecimal é: {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente!')
