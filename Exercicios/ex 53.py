frase = str(input('Digite um frase: ')).strip().upper() #para padronizar o texto em maiusculas
palavras = frase.split() #para separar por palavras em uma lista
junto = ''.join(palavras) #para juntar todo o texto
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print ('É UM PALÍNDROMO')
else:
    print ('NÃO É PALÍNDROMO')
