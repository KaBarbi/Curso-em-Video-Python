#43- desenvolva uma logica que leia o peso e a altura de uma pessoa e calcule seu imc, mostrando seu status de acordo:

#- abaixo de 18.5: abaixo do peso
#- entre 18.5 e 25: peso ideal
#- 25 ate 30: sobrepeso
#- 30 ate 40: obesidade
#- acima de 40 obesidade mórbida

p = float(input('Digite seu peso em kg: '))
a = float(input('Digite sua altura em cm: '))

imc = float(p / (a ** 2))

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesisdade morbida')

print('Seu imc é {:.2f}'.format(imc))