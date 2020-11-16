from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range (1,7+1):
    ano = int(input('Em que ano a {}º nasceu? '.format(pessoa)))
    idade = atual - ano
    if idade >= 18:
        maior = maior +1
    else:
        menor = menor + 1
print('{} são maiores de idade e {} são menores'.format(maior,menor))