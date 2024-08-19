#36- Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabando que não pdoe exeder 30% do salario ou então o emprestimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual seu salario? R$ '))
anos = int(input('Em quantos anos vai pagar? '))

prestacao = casa / (anos * 12)

minimo = sal * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo Negado!')