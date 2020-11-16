soma = 0
conta = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        conta = conta + 1
print('Você informou {} números Pares e a soma é de {}'.format(conta,soma))