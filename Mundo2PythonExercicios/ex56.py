# 56- Desenvolva um programa que leia nome idade e sexo de 4 pessoas, no final deve:
# - Mostrar a media da idade de todos
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('--------{} PESSOA ---------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1

mediaidade = somaidade / 4
print('A mdeia de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos é {}'.format(totmulher20))