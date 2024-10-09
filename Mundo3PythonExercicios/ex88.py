#Faça um programa que ajude um jogador da mega sena a criar palpites.
#O programa vai perguntar quantas jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta.

import random

def gerar_jogos_megasena(quantidade):
    jogos = []
    for _ in range(quantidade):
        jogo = set()
        while len(jogo) < 6:
            numero = random.randint(1, 60)
            jogo.add(numero)
        jogos.append(sorted(list(jogo)))
    return jogos

quantidade_jogos = int(input("Quantos jogos você quer gerar? "))

jogos_gerados = gerar_jogos_megasena(quantidade_jogos)

print("\nSeus jogos da Mega-Sena:")
for i, jogo in enumerate(jogos_gerados):
    print(f"Jogo {i+1}: {jogo}")