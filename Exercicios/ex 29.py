from random import randint
print('Bom dia :)')
vel = randint(40,120)
if vel >80:
    print('Chegou uma multa aqui para você')
    print('A multa foi de R${}'.format((vel-80)*7))
    # opcional -> multa = (velocidade - 80)*7
    # opcional -> ('A multa foi de R${}'.format((multa))
    print('Você excedeu a velocidade máxima em {}km/h'.format(vel-80))
    # opcional -> velo excedente = (velocidade - 80)
else:
    print('Bom dia!')

