#termo = vezes = n = 0
termo = 0
vezes = 0
n = 0
n = int(input('Digite um número [999 para parar]: ')) # dessa forma o 999 não entra
while n != 999:
    termo = termo + n
    vezes = vezes + 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(vezes,termo)) # ou .format(vezes - 1, termo - 999)