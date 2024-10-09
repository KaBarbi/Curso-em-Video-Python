#Aprimore o desafio anterior, mostrando no final:
#A- A soma de todos os valores pares digitados.
#B- A soma dos valores da terceira coluna
#C- O maior valor da segunda linha


matriz = []
soma_pares = 0
soma_terceira_coluna = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))
        linha.append(valor)

        if valor % 2 == 0:
            soma_pares += valor

        if j == 2:
            soma_terceira_coluna += valor
    matriz.append(linha)


for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end="")
    print()

maior_segunda_linha = max(matriz[1])

print(f"\nA soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")