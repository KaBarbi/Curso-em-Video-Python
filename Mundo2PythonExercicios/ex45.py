# 45- crie um programa que faça o programa jogar jokempo com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opçoes:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual é sua jogada?: '))
print('-=' * 15)
print('O Jogador jogou {}'.format(itens[jogador]))
print('O Computador jogou {}'.format(itens[computador]))
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print('COPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')