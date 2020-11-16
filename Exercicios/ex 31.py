kms = float(input('Quantos kms tem a viagem?'))
print('E quanto te custou o bilhete?')
if kms <= 200:
    ticket = kms * 0.50
    print('O bilhete me saiu R${:.2f}'.format(ticket))
else:
    ticket = kms * 0.545
    print('O bilhete me saiu R${:.2f}'.format(ticket))

#kms = float(input('Quantos kms tem a viagem?'))
#print('E quanto te custou o bilhete?')
#ticket = kms * 0.50 if km <= 200 else kms * 0,45
#print('O bilhete me saiu R${:.2f}'.format(ticket))