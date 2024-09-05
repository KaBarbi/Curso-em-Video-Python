#67- faça um programa que mostre a tabuada de vários números, um de cada vez
# para cada valor digitado pelo usuário. O programa será interrompido quando o numero solicitado for negativo.

while True:
    n = int(input('Digite o numero da tabuada: '))
    if n < 0:
        break
    print('-' *30)
    for i in range(1, 11):
        print(f'{n} X {i} {n*i}')
    print('-' * 30)
print('PROGRAMA ENCERRADO!')