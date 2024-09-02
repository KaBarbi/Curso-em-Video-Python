# 59- Crie um programa que leia 2 valores e mostre um menu na tela:
# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos números
# 5 sair do programa
# seu programa devera realizar a operação solicitada em cada caso.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:

    print("\nMenu de Opções:")
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Maior")
    print("4. Novos números")
    print("5. Sair do programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = num1 + num2
        print("A soma é:", resultado)
    elif opcao == 2:
        resultado = num1 * num2
        print("A multiplicação é:", resultado)
    elif opcao == 3:
        maior = max(num1, num2)
        print("O maior número é:", maior)
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
    print(':=:' * 10)
