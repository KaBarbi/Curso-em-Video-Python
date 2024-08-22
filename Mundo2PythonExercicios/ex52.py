# 52- Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

n = int(input('Digite um numero: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\no numero {} foi divisivel {} vezes!'.format(n, tot))
