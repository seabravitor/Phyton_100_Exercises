from time import sleep
from datetime import date
print ('-'*40)
print ('CENTRAL DE CADASTROS')
homem = mulher = menorid = maiorid = terceiraid = hmenorid = fmenorid = 0
qtd = 0
parar = 'S'
sexo = ' '
atual = date.today().year
while parar in 'Ss':
    print('-' * 40)
    pessoa = str(input('Qual é o seu nome? ')).strip().upper()[0]
    ano = int(input('Qual é seu ano de nascimento? '))
    idade = atual - ano
    if idade < 18:
        menorid = menorid + 1
    elif idade >= 18:
        maiorid = maiorid + 1
    elif idade >= 70:
        terceiraid = terceiraid + 1
    while sexo not in 'MmFf':
        sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()
        if sexo in 'Mm':
            homem = homem + 1
        elif sexo in 'Ff':
            mulher = mulher + 1
    print('Cadastrado com sucesso')
    sleep(1)
    print ('-'*40)
    parar = str(input('Quer fazer um novo cadastro? [S/N] ')).upper().strip()
    qtd = qtd + 1
print('Obrigado por participar')
sleep(1)

if sexo in 'Mm' and idade < 18:
    hmenorid = hmenorid + 1
elif sexo in 'Ff' and idade < 18:
    fmenorid = fmenorid + 1

print('Resultado dos cadastros')
print('Total Cadastrados: {}'.format(qtd))
print('{} Sexo Masculino e {} Sexo Feminino'.format(homem,mulher))
print('{} Menores de Idades, {} Maiores de Idade e {} Terceira Idade'.format(menorid,maiorid,terceiraid))
print('{} Homens menores de idade e {} Mulheres menores de idade'.format(hmenorid,fmenorid))

