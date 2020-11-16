from random import uniform
print ('{:=^40}'.format(' LOJAS LEVE AGORA '))
print('ESCOLHA A FORMA DE PAGAMENTO')
print ('~'*40)
print('''[1] Á vista no dinheiro: 10% de desconto.
[2] Á vista no cartão: 5% de desconto
[3] Em 2x no cartão: Sem Juros
[4] Em 3x no cartão: 20% de Juros''')
print ('~'*40)
preço = (uniform(10,5000))
print ('Valor Total do Produto = R${:.2f}'.format(preço))
forma = int(input('Digite a forma de pagamento escolhida: '))
if forma == 1:
    p1 = preço * 0.90
    print('O valor final do produto é R${:.2f}. Dirija-se até o caixa.'.format(p1))
elif forma == 2:
    p2 = preço * 0.95
    print('O valor final do produto é R${:.2f}. Insira seu cartão'.format(p2))
elif forma == 3:
    p3 = preço / 2
    print('O valor da parcela será de {:.2f}. Prossiga com o pagamento ao inserir seu cartão.'.format(p3))
elif forma == 4:
    p4 = preço * 1.2
    parcela4 = p4/3
    print('O preço final do produto é {:.2f}. Cada parcela sairá no valor de {:.2f}. Prossiga com o pagamento ao inserir seu cartão.'.format(p4,parcela4))
else:
    print('Forma de pagamento inválida')
print('Obrigado e volte sempre')