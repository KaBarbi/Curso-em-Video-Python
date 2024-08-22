#49- Refaça o exercício 9, mostrando a tabuada de um numero que o usuário escolher só que agora utilizando o for.

num = int(input('DIgite um numero para ver sua tabuada: '))
for i in range(11):
    print('{} X {:2} = {}'.format(num, i, num*i))