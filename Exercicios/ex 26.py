frase = str(input('Digite uma frase de impacto:')).upper().strip()
#upper para contar maiuscula e miniscula
#split para não contar espaços indesejados
print('A letra a aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira vez que aparece a é na posição {} da frase'.format(frase.find('a')+1))
#+1 serve para buscar a primeira
print('A ultima vez que aparece a é na posição {} da frase'.format(frase.rfind('A')+1))
#rfind para buscar do começo para o fim
