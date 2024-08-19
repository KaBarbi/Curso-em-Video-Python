# 37 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um numero inteiro: '))
print('''Escohla qual Base de conversão usar:
[1] Binario834
[2] Octal
[3] Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(' {} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para ocar é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!')