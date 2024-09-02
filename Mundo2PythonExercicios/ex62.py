#62- Melhore o desafio 61, perguntando para o usuário se ele quer mostra mais alguns termos. o programa encerra quando ele disser que quer mostra 0 termos.

print('Gerador de PA')
print('-:-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= 10:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print(f'Progressao total dinalizada com {termo} termos mostrados!')
print('FIM!')