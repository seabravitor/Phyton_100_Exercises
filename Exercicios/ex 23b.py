num = int(input('Diga um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O seu número aleatório é: {}'.format(num))
print('O milhar é {}'.format(m))
print('A centena é {}'.format(c))
print('A dezena é {}'.format(d))
print('A unidade é {}'.format(u))
