#39 - faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#- se ele ainda vai se alistar no exercito
#- se é hora de se alistar no exercito
#- se já passou do tempo de se alistar.
#seu programa devera mostrar tbm quando falta ou passou do prazo

from datetime import date
atual =date.today().year
nasc = int(input('Qual ano voce nasceu: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(('Faltam {} anos para se alistar.'.format(saldo)))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce ja deveria ter se alistadao há {} anos.'.format(saldo))
    print('Seu alsitamento foi {}'.format(ano))