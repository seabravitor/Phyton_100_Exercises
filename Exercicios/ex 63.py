print('='*22)
print('SEQUÊNCIA DE FIBONACCI')
print('='*22)
termos = int(input('Quantos termos você quer calcular? '))
t1 = 0
t2 = 1
print('{:=^22}'.format('RESULTADO'))
print('{} - {}'.format(t1,t2),end='')
cont = 3 #vai contar a partir do número 3
while cont <= termos:
    t3 = t1 + t2
    t1 = t2 #passa a ser o valor do seguinte
    t2 = t3 #passa a ser o valor do seguinte
    print(' - {}'.format(t3),end='')
    cont = cont + 1
print('- FIM')