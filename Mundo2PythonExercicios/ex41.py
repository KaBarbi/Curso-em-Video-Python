# 41 - a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - ate 9 anos Mirim
# - ate 14 infantil
# - ate 19 júnior
# - ate 20 sênior
# - acima master

ano = int(input('Qual ano voce nasceu? '))
idade = 2024 - ano

if idade <= 9:
    print('Voce esta na categoria mirim!')
elif idade > 9 and idade <= 14 :
    print('Voce esta na categoria infantil!')
elif idade > 14 and idade <= 19 :
    print('Voce esta na cetegoria junior!')
elif idade > 19 and idade <= 20 :
    print('Voce esta na categoria senior!')
else:
    print('Voce esta na categoria master!')

print(idade)