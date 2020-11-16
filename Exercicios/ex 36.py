print ('Olá, seja bem vinda ao Banco Digital')
casa = float(input('Vejo que busca um empréstimo, ótimo! Qual é o valor da casa?'))
sal = float(input('E o seu salário liquido mensal? '))
anos = float(input('Em quantos anos pretende pagar? '))
pres = casa / (anos*12)
print ('Certo! O valor de prestação, sem contar os juros, será de {}'.format(pres))
if pres >= sal*0.3:
    print ('Com essas condições, o empréstimo não será concedido.')
else: print ('Parabéns, aqui está seu empréstimo')