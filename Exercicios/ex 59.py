from time import sleep
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
opt = 0
while opt != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opt = int(input('ESCOLHA UMA OPÇÃO: '))
    if opt == 1:
        soma = n1 + n2
        print ('O resultado é {}'.format(soma))
    elif opt == 2:
        produto = n1 * n2
        print('O resultado é {}'.format(produto))
    elif opt == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre os escolhidos é {}'.format(maior))
    elif opt == 4:
        print('Informe dois novos números')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente')
    print ('=-='*10)
    sleep(2)
print('Obrigado! Volte sempre')