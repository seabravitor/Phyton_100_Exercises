import random
aluno1 = str(input('Nome do Aluno 1: '))
aluno2 = str(input('Nome do Aluno 2: '))
aluno3 = str(input('Nome do Aluno 3: '))
aluno4 = str(input('Nome do Aluno 4: '))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('Entre os alunos, {}, {}, {},{}. Quem vai apagar o quadro hoje é: {}'.format(aluno1,aluno2,aluno3,aluno4,escolhido))
