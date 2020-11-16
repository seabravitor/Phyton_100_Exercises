sal = float(input('Qual é o seu salário mensal? R$ '))
if sal <= 1250:
    aum = sal+(sal*0.15)
else:
    aum = sal+(sal*0.10)
print ('Você sabia que na virada do ano seu salário passará a ser de R${}?'.format(aum))