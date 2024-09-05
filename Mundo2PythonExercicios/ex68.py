# 68- Faça um programa que jogue par ou impar com o computador
# o jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivos.


import random

def jogo_par_ou_impar():
    vitorias = 0

    while True:
        escolha_jogador = input("Escolha par ou ímpar: ").lower()
        while escolha_jogador not in ['par', 'impar']:
            print("Escolha inválida. Digite 'par' ou 'impar'.")
            escolha_jogador = input("Escolha par ou impar: ").lower()

        numero_jogador = int(input("Digite um número entre 1 e 10: "))
        while numero_jogador < 1 or numero_jogador > 10:
            print("Número inválido. Digite um número entre 1 e 10.")
            numero_jogador = int(input("Digite um número entre 1 e 10: "))

        numero_computador = random.randint(1, 10)
        soma = numero_jogador + numero_computador
        resultado = "par" if soma % 2 == 0 else "impar"

        print(f"O computador escolheu {numero_computador}.")
        print(f"A soma é {soma}, que é {resultado}.")

        if (resultado == escolha_jogador):
            print("Você ganhou!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break

    print(f"Você teve {vitorias} vitórias consecutivas.")

jogo_par_ou_impar()