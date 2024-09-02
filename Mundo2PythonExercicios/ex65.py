# faça um programa que leia varios numeros e no final mostre a media entre todos e qual foi maior e qual foi menor.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n



    resp = str(input('Quer continuar? [S/N] ')).upper()
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}.')
