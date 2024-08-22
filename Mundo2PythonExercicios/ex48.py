# 48- Faça um programa que calcule a soma de todos os números impares que são múltiplos de 3 e que se encontram entre 1 ate 500.

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print('A soma de todos os {} valores é {} '.format(cont, soma))