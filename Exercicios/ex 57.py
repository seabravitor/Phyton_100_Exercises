sexo = str(input('Escolha um sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo Inválido. Por favor, escolha um sexo [M/F]:')).strip().upper()[0]
print('Cadastrado com Sucesso')