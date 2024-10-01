#Crie uma tupla preenchida com os 20 primeiros colocados do brasileirão, na ordem de colocação. Depois mostre:
#A- apenas os 5 primeiros colocados
#b- os últimos 4 colocados
#c- uma lista com os times em ordem alfabética
#d- Em que posição na tabela esta o time da chapecoense

times_brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fluminense',
                   'Corinthians', 'Internacional', 'São Paulo', 'Grêmio', 'Fortaleza',
                   'Botafogo', 'Santos', 'Ceará', 'Bahia', 'Goiás',
                   'Cuiabá', 'América-MG', 'Coritiba', 'Avaí', 'Juventude')

primeiros_5 = times_brasileirao[:5]
print("Os 5 primeiros colocados são:", primeiros_5)

ultimos_4 = times_brasileirao[-4:]
print("Os últimos 4 colocados são:", ultimos_4)

times_alfabetica = sorted(times_brasileirao)
print("Os times em ordem alfabética são:", times_alfabetica)

try:
    posicao_chapecoense = times_brasileirao.index('Chapecoense') + 1
    print("A Chapecoense está na posição:", posicao_chapecoense)
except ValueError:
    print("A Chapecoense não está entre os 20 primeiros colocados.")