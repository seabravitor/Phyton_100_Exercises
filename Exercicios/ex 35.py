print('~'*20)
print('Analisador de Triângulos')
print('~'*20)
r1 = float(input('Primeira reta em cm: '))
r2 = float(input('Segunda reta em cm: '))
r3 = float(input('Terceira reta em cm: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo')
else: print('As retas não podem formar um triângulo')
t