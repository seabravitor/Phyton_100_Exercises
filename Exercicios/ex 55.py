maior = 0
menor = 0
for pessoa in range (1,5+1):
   peso = float(input('Qual é o peso da {}º pessoa? '.format(pessoa)))
   if pessoa == 1:
       maior = peso
       menor = peso
   else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print('O maior peso é {:.2f}Kg'.format(maior))
print('O menor peso é {:.2f}Kg'.format(menor))
#NÃO PODERIA TENTAR COM LISTA????
