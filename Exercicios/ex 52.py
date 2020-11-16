n1 = int(input('Digite um número: '))
total = 0
for c in range(1,n1+1):
    if n1 % c == 0:
        print('\033[33m',end='')
        total = total + 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c),end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n1,total))
if total == 2:
    print('É um número primo')
else:
    print('Não é primo')