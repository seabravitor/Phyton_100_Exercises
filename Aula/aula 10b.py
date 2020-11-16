n1 = float(input('Qual foi a nota da Karol no primeiro bimestre?'))
if n1 <=5:
    print('Eita vida!')
n2 = float(input('E a do segundo?'))
if n2 <=5:
    print('Puta merda')
m = (n1 + n2)/2
print('A média dela foi de {:.1f}?'.format(m))
print('Sim')
print('Isso significa que ela vai ter que fazer recuperação?')
if m <=6:
    print('Pois é, infelizmente')
    print ('Filha da mãe!!! Ela vai ver só uma coisa')
else:
    print('Não, ela passou direito')
    print('Ufa, que bom! Boa menina')
print('Obrigada Professora')
