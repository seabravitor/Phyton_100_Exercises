n1 = float(input('Rachel! Qual foi a sua nota no primeiro bimestre? '))
n2 = float(input('E a do segundo? '))
média = (n1 + n2)/2
if média < 5.0:
    print('Puta que pariu menina! Com {:.2f}, você vai Reprovar'.format(média))
elif 5.0 <= média < 7.0:
    print('Daaale espertona!! Show de bola, com essa vergonha ai de {:.2f}, você fica recuperação'.format(média))
else:
    print('Não faz nada mais do que a obrigação, com essa média de {:.2f}, você foi aprovado'.format(média))