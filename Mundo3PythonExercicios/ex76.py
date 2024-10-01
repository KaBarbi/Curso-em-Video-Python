#Crie um progama que tenha uma tuopla com nokmes de produtos e seus preços na sequencia
# no ifnal mostre uma listagem com precos organizando os dados de forma tabular

produtos_e_precos = (
    ("Caderno", 15.99),
    ("Lápis", 2.50),
    ("Caneta", 3.99),
    ("Borracha", 1.25),
    ("Régua", 5.99)
)

# Encontrar o maior nome para ajustar o tamanho das colunas
maior_nome = max(len(produto) for produto, _ in produtos_e_precos)

# Cabeçalho da tabela
print(f"{'Produto':^{maior_nome}} | Preço")
print("-" * (maior_nome + 1 + 6))  # Linha divisória

# Corpo da tabela
for produto, preco in produtos_e_precos:
    print(f"{produto:^{maior_nome}} | R$ {preco:.2f}")