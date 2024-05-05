ativos = []
# Entrada da quantidade de ativos
quantidadeAtivos = int(input())
# Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# Ordenar os ativos em ordem alfabética.
ordenado = sorted(ativos)
# Imprimir a lista de ativos ordenada, um por linha
for ativo in ordenado:
    print(ativo)
