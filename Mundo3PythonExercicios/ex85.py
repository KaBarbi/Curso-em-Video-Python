#Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e impares. no final, mostre em ordem crescente

numeros = []
pares = []
impares = []

for i in range(7):
    numero = int(input("Digite o {}º número: ".format(i+1)))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print("\nNúmeros pares em ordem crescente:")
for numero in pares:
    print(numero)

print("\nNúmeros ímpares em ordem crescente:")
for numero in impares:
    print(numero)
