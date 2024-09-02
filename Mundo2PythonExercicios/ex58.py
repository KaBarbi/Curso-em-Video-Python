# 58- Melhore o Jogo do desafio 28 onde o computador vai pensar em um numero.

from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue advinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez.')

        elif jogador > computador:
            print('Menos... tente outra vez.')

print(F'Voce acertou!, voce levou {palpites} tentativas!')