# Lista para armazenar os itens
itens = []

while len(itens) < 3:
    itemList = input()
    itens.append(itemList)
# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")