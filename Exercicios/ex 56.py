somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for pessoa in range (1,4+1):
    print ('----------{}º PESSOA----------'.format(pessoa))
    nome = str(input('Nome: ')).strip() #tirar espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
#REVER