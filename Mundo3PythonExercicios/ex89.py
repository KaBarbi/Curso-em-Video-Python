#Crie um programa que leia o nome de duas notas de varios alunmos e guarde tudo em uma lista composta.
#No final mostre um boletim contendo a media de cada um e permita que o usuário possa mostra as notas de cada aluno individualmente.

boletim = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, nota1, nota2, media])

print("\nBoletim:")
for aluno in boletim:
    print(f"Aluno: {aluno[0]} - Média: {aluno[3]}")

while True:
    consulta = input("\nDeseja ver as notas de algum aluno? (sim/não): ")
    if consulta.lower() == 'não':
        break
    nome_consulta = input("Digite o nome do aluno: ")
    aluno_encontrado = False
    for aluno in boletim:
        if aluno[0].lower() == nome_consulta.lower():
            print(f"Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}")
            aluno_encontrado = True
            break
    if not aluno_encontrado:
        print("Aluno não encontrado.")