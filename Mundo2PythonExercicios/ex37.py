#37 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

n = float(input('Digite um numero: '))
escolha = int(input('Escolha qual base de conversão iŕa usar: 1- Binario, 2- Octal, 3- hexadecimal: '))

if escolha == 1:
    binario = bin(n)
    print(binario)