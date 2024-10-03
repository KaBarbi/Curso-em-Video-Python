# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo devera analisar se a expressão passada esta com os parênteses abertos e fechados na ordem correta.

expr = str(input('DIgite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta invalida')