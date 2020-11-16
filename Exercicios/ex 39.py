from datetime import date
atual = date.today().year
nasc = int(input('Que ano você nasceu?'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'. format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar no exército!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alisamento foi em {}.'.format(ano))