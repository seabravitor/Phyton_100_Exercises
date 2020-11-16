# from math import factorial
# print ('{:=^60}'.format('Calculadora de Fatorial'))
# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n,f)

# print ('{:=^60}'.format('Calculadora de Fatorial'))
# n = int(input('Escolha um número: '))
# resultado = 1
# gap = 1
#while gap <= n:
#    resultado *= gap
#    gap += 1
#print('O fatorial do número {}! é {}.'.format(n,resultado))

print ('{:=^60}'.format('Calculadora de Fatorial'))
n = int(input('Escolha um número: '))
c = n
f = 1
print('Calculando {}! = '.format((n), end='')
while c > 0:
    print ('{}'.format(c), end='')
    print (' x ' if c > 1 else '=', end ='')
    f *= c
    c -= 1
print('{}'.format(f))