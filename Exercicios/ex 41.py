from datetime import date
atual = date.today().year
anon = int(input('Qual é o ano de nascimento do atleta? '))
idade = atual - anon
if idade <= 9:
    print('Com {} anos, O atleta está na categoria MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Com {} anos, o atleta se enquadra na categoria INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Com {} anos, o atleta está na catefogira JUNIOR'.format(idade))
elif 19 < idade <= 40:
    print('O atleta com {} anos, se encontra na categoria ADULTO'.format(idade))
elif idade > 40:
    print('Com {} anos, sua categoria é a MASTER'.format(idade))