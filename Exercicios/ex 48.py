soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:
        cont = cont + 1 #contador a cada um
        soma = soma + c #acumula somando os valores
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))