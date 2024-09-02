#57- Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ‘F’. Caso esteja errado, peça a digitação novamente ate ter um valor correto.


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
  sexo = str(input('Dados invalidos!, por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(F'Sexo {sexo} registrado com sucesso!')