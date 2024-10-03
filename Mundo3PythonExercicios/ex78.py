#faça um programa que leia 5 valores numéricos e guarde em uma lista. No final mostre qual foi o maior valor e o menor valor e seu respectiva posição na lista


listaum = []
mai = 0
men = 0


for i in range(0, 5):
    listaum.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        mai = men = listaum[i]
    else:
        if listaum[i] > mai:
            mai = listaum[i]
        if listaum[i] < men:
            men = listaum[i]



print('=-' * 30)
print(f'Voce digitou os valores {listaum}')
print(f'O maior valor digitado foi {mai}  nas posições: ', end='')
for c, v in enumerate(listaum):
    if v == mai:
        print(f'{c}... ', end='')
print()
print(f'O menor valor digitado foi {men}  nas posições: ', end='')

for c, v in enumerate(listaum):
    if v == men:
        print(f'{c}... ', end='')
print()
