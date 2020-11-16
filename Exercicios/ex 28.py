from random import randint
print ('Seja todos bem vindos a Loteria Bolão')
print ('Hoje quem adivinhar o número entre 0 e 5, leva o prêmio para casa')
print ('Vamos começar')
v = int(input('Vitor, qual é o seu número?'))
k = int(input('Karol, sua vez de adivinhar, qual é a sua escolha?'))
sort = randint(0, 5)
print('E o número sorteado é: {}'.format(sort))
if v == sort:
    print('Parabéns Vitor! Você ganhou!')
if k == sort:
    print('Parabéns Karol, o prêmio é todo seu!')
else:
    print(' E o prêmio acumula mais uma vez!')
print('Obrigado a todos! Até a próxima')



