#51- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão. (progressão aritmética)

n = int(input('Digite o peimeiro termo:'))
razao = int(input('Razaão: '))
decimo = n + (10 - 1) * razao

for i in range(n, decimo + razao, razao):
    print('{}'.format(i), end = ' -> ')
print('FIM')
