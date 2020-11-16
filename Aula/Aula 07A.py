n1=int(input('Escolha um valor: '))
n2=int(input('Escolha outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1**n2
sobra=n1%n2
print('A soma vale {}, o produto é {}, a divisão {}, a potência é {}, a divisão direta é {} com sobra {}'.format(s,m,d,p,di,sobra), end=' ')
print('A divisão com 3 numeros após a virgula é {:.3f}'.format(d))