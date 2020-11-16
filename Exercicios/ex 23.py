import random
ram = int(input(random.randrange(0,9999)))
u = ram // 1 % 10
d = ram // 10 % 10
c = ram // 100 % 10
m = ram // 1000 % 10
print('O seu número aleatório é: {}'.format(ram))
print('O milhar é {}'.format(m))
print('A centena é {}'.format(c))
print('A dezena é {}'.format(d))
print('A unidade é {}'.format(u))

