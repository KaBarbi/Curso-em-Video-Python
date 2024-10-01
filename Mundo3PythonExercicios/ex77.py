#Crie uma tupla que tenha varias palavras( sem acentos), Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('ARROZ', 'FEIJAO', 'LINGUICA', 'BATATA', 'TOMATE')
vogais = 'AEIOU'

for palavra in palavras:
    print(f"Palavra: {palavra}")
    print("Vogais:", end=" ")
    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")
    print()