# 40 - crie um programa que leia 2 notas de um aluno e calcule sua media. mostrando uma mensagem no final de acordo com a media atingida:

# abaixo de 5 reprovado
# entre 5.0 e 6.9 recuperação
# media 7.0 ou maior aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) /2

if media <= 5:
    print('Reprovado!')
elif media > 5 and media <= 6.9:
    print('Recuperação')
elif media >= 7.0 :
    print('Aprovado!')

print(media)