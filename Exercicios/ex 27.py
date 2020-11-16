n = str(input('Escreva seu nome completo:')).strip()
nome = n.split()
#n.split para dividir entre os nomes
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
#len é usado para contar a quantidade de nomes -1 para buscar o último
