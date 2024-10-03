# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A- quantos números foram digitados.
# B- a lista de valores ordenada de forma decrescente.
# C- se o valor 5 foi digitado e esta ou não na lista.

valores = []
while True:
    valores.append(int(input('Digite um Valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
valores.sort(reverse=True)

print(f'Voce digitou {len(valores)} elementos.')
print(f'Os valores em ordm decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lsita!')
else:
    print('O valor  5 nao foi encontrado na lista.')