#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final mostre a matriz na tela, com a formatação correta

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end="")
    print()