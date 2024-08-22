# 53- Crie um programa que lia uma frase qualquer e diga se ela é um palíndromo.
# (EX: o lobo ama o bolo, após a sopa)

f = str(input('Digite uma frase: '))
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
inverso =junto[::-1]

'''for letra in range(len(junto), -1, -1, -1):
    inverso += junto[letra]'''

print('o inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')
