from time import sleep
print('-'*40)
print('{: ^40}'.format('LOJA BARATÃO'))
print('-'*40)
qtd = total = pmax = pmin = 0
caixa = 'N'
barato = ''
caro = ''
while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Valor: R$'))
    total = total + valor
    qtd += 1
    if qtd == 1:
        pmax = valor
        caro = produto
    else:
        if valor > pmax:
            pmax = valor
            caro = produto
    if qtd == 1:
        pmin = valor
        barato = produto
    else:
        if valor < pmin:
            pmin = valor
            barato = produto
    caixa = str(input('Quer fechar a compra? [S/N]')).strip().upper()[0]
    if caixa in 'Ss':
        break
sleep(1)
print('{:-^40}'.format('CAIXA'))
print('O valor total da compra de {} produtos, é: R${}'.format(qtd,total))
print('O produto mais caro é o {} no valor de {}.'.format(caro,pmax))
print('O produto mais barato é o {} no valor de {}.'.format(barato,pmin))
print('Obrigado, volte sempre!')


