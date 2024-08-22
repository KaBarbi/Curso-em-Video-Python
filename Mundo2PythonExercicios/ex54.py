# 54- Crie um programa que leia o ano de nascimento de 7 pessoas e informe quantas já atingiram a maior idade e quantas ainda não. (21 anos)

from datetime import date
from itertools import repeat

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pa {}° pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade >=21:
        totmaior +=1
    else:
        totmenor +=1
    print('Maiores de idade: {}'.format(totmaior))
    print('Menores de idade: {}'.format(totmenor))