nome = str(input('Qual é o seu nome? '))
#simples
if nome == 'Vitor':
    print ('Que nome top!!!')
#aninhada
elif nome == 'Tiago' or nome == 'Maria' or nome == 'João':
    print ('Seu nome é bem comum no Brasil.')
#composta
else: print ('Sem Graça :(')
print ('Tenha um bom dia {}'.format(nome))