n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
n3 = int(input('Escolha um último número: '))
#menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print ('O maior número escolhido foi: {} '.format(maior))
print ('O menor número entre os escolhidos é: {} '.format(menor))