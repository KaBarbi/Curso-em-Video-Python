#66- faça um programa que leia vários números e só pare ao digitar 999, no final mostre a quantidade de números e a soma deles.

n = soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Voce digitou {cont} numeros e a soma deles é {soma}')