# 70- crie um programa que leia o nome e preço de vários produtos. O programa deve perguntar se o usuário quer continuar, no final mostre:
# Qual o total gasto na compra
# Quantos produtos custam mais de 1000 reais
# Qual é o nome do produto mais barato

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resp == 'n':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos que custam maior que R$10000.00.')
print(f'O profurto mais barato foi {barato} que custa R${menor:.2f}')
