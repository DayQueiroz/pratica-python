lista = [1, 4, 3, 1, 6, 5, 3]

print(f"Tipo da lista: {type(lista)}")
print(lista)

conjunto_convertido = set(lista)

print(f"Tipo do conjunto convertido: {type(conjunto_convertido)}")
print(conjunto_convertido)

lista_convertida = list(conjunto_convertido)

print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)

# Quando convertemos a lista para conjunto, que aqui usamos o 'set',
# ele traz a listagem sem numeros convertidos.
# Quando convertemos de conjunto para lista, se mantem a lista sem os numero repetidos do conjunto.