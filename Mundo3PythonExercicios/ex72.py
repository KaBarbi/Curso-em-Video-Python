# crie uma tupla totalmente preenchida com uma contagem por extensão, de zero ate 20
# Seu programa devera ler um numero pelo teclado e(entre 0 e 20), e mostra-lo por extensão

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                       'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"O número {numero} por extenso é: {cont[numero]}")
        break
    else:
        print("Número inválido. Tente novamente.")
