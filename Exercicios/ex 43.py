peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura, em metros?'))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Isso significa que você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Isso significa que você está no peso ideal')
elif 25 <= imc < 30:
    print('Isso significa que você está sobrepeso')
elif 30 <= imc < 40:
    print('Isso mostra que você está obeso')
elif imc >= 40:
    print('Você tem obesidade mórbida')