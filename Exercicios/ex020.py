import random
# or from random import shuffle
ap1 = str(input('Karol, sua apresentação de hoje será sobre o quê?'))
ap2 = str(input('João, e a sua?'))
ap3 = str(input('Vitor, a sua será sobre qual tema?'))
ap4 = str(input('E por úlitmo, do que você falará, Robertinho?'))
lista = [ap1,ap2,ap3,ap4]
random.shuffle(lista)
#shuffle (lista)
print('A ordem de apresentação então será:')
print(lista)