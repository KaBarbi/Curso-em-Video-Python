#Programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A- quantas vezes o numero 9 apareceu
#B- Em que posição foi digitado o primeiro valor 3.
#C- quais foram os numeros pares.

numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os números pares digitados foram:', end='')
for n in numeros:
    if n % 2 == 0:
        print(f' {n}', end='')
print()