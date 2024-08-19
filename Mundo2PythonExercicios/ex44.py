# 44- Elabora um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:

# - a vista 10% de desconto (cheque e din apenas)
# - a vista cartão 5% desconto
# - 2x no cartão preço normal
# - 3x ou mais no cartão 20% juros
print('{::^40}'.format(' LOJA BARBI '))
preco = float(input('Preço das compras: R$ '))
print('''Formas de Pagamento:
[1] à vista dinheiro/ cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual opção você deseja?: '))

if opcao == 1:
    total = preco * 0.9  # Desconto de 10%
elif opcao == 2:
    total = preco * 0.95  # Desconto de 5%
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco * 1.2  # Acréscimo de 20%
    totparc = int(input('Quantas parcelas? '))
    while totparc < 3:  # Validação do número de parcelas
        print('O número mínimo de parcelas para essa opção é 3.')
        totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('Opção inválida!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))