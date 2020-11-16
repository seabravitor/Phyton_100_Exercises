ano = int(input('Olá Menina do Futuro! Você veio de que ano?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('Legal, esse é um ano bisexto')
else:
    print('Legal')