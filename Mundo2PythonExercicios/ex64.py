#64- Crie um programa que leia vários números inteiros pelo teclado. o programa só vai para quando o usuário digitar o valor 999,
#que é a condição de parada. no final  mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)

n = soma = cont = 0

while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        cont += 1
        soma += n

print(f'A quantidade de números digitados foi \033[0;33m{cont}\033[m e a soma foi \033[0;31m{soma}\033[m')