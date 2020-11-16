print ('{:=^40}'.format('GERADOR DE PA'))
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n #termo inicio com n
c = 1 #contagem de termo em termo (?)
total = 0
segue = 10
while segue != 0:
    total = total + segue
    while c <= total: #total termos
        print ('{} -> '.format(termo),end='')
        termo = termo + r #resultados
        c = c + 1 #why?
    print('PAUSA')
    segue = int(input('Quer ver mais termos? Quantos mais? ' ))
print('Progressão finalizada com {} termos em tela'.format(total))
