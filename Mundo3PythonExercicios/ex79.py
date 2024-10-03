# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre em uma lista,
# caso o numero já exista lá dentro ele não será adicionado. No final serão exibidos todos valores únicos digitados em ordem crescente.


numeros = list()
while True:
    n = int(input('Gigite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionado com sucesso.')
    else:
        print('Valor duplicado!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
