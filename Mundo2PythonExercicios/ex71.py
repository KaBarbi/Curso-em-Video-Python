# 71- Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1

print(':' * 40)

valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de RD{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(':' * 40)
