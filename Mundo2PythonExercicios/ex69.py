# 69- Crie um programa que leia a idade e sexo de varias pessoas, a cada pessoa cadastrada o programa deve perguntar se quero continuar ou não, no final o programa deve mostrar:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'mf':
        sexo = input('Sexo: [m/f]: ').strip().lower()
    if idade >= 18:
        tot18 += 1
    if sexo == 'm':
        totH += 1
    if sexo == 'f' and idade < 20:
        totM20 += 1
    resp = ''
    while resp not in 'sn':
        resp = input('Quer continuar? [s/n]: ').strip().lower()
    if resp == 'n':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Temos {totM20} mulheres com menos de 20 anos.')
