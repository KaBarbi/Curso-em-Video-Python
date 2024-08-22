# 50- Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas dos que forem pares.

soma = 0
cont = 0
for i in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print('VOde infromou {} numeros pares e a soma deles é {}'.format(cont, soma))