from random import randint
print('=-'*20)
print('JOGO DO PAR OU ÍMPAR - Entre 0 e 10')
print('=-'*20)
comp = randint(0, 10)
num = int(input('Digite um valor: '))
jogo = str(input('Par ou Ímpar? ')).upper().strip()
somaresultado = comp + num
v = 0
qtd = 0
if somaresultado % 2 == 0:
        resultado = 'PAR'
else:
        resultado = 'ÍMPAR'
while resultado == jogo:
    print('=' * 20)
    v = v + 1
    qtd = qtd + 1
    print('{}. VOCÊ GANHOU. Seu jogo foi {} e o meu {} - TOTAL {}.'.format(resultado,num,comp,somaresultado))
    print('Vamos jogar denovo!!!')
    print('=' * 20)
    num = int(input('Digite um valor: '))
    jogo = str(input('Par ou Ímpar? ')).upper().strip()
else:
    print('=' * 20)
    qtd = qtd + 1
    print('{}. VOCÊ PERDEU. Seu jogo foi {} e o meu {} - TOTAL {}.'.format(resultado,num,comp,somaresultado))
    print('=' * 20)
    print('Game over! De {}, Você ganhou {}. Até a próxima.'.format(qtd,v))

'''
v= 0
While True:
    num = int(input('Digite um valor: '))
    comp = randint(0, 10)
    somaresultado = comp + num
    jogo = ''
    While jogo not in 'PI':
        jogo = str(input('Par ou Ímpar? ')).upper().strip()
    print('Você jogou {num} e o computador {comp}. Total de {somaresultado}')
    if jogo == 'P':
        if somaresultado % 2 == 0:
        print('Você venceu)
        v +=1
        else:
        print('Você perdeu')
        break
    elif tipo == 'I':
        if somaresultado % 2 == 0:
        print('Você venceu)
        v +=1
        else:
        print('Você perdeu')
        break   
    print('Vamos jogar novamente')
print('Você vencer {} vezes'.format(v))'''