from random import randint
sort = randint(0, 10)
print ('Seja todos bem vindos a Loteria Bolão')
print ('Hoje quem adivinhar o número entre 0 e 10, leva o prêmio para casa')
print ('Vamos começar')
certa = False
tentativas = 0
while not certa:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if palpite == sort:
        certa = True
    else:
        if palpite > sort:
            print('Menos... Tente novamente: ')
        elif palpite < sort:
            print ('Mais... Tente novamente: ')
print('Parabéns! Você acertou com {} tentativas'.format(tentativas))
