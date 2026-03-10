paises = ["Brasil", "Argentina", "Canadá"]

print("Lista original")
print(paises)

paises.append("Portugal")

print("Após adicionar novo país")
print(paises)

paises.insert(1, "Espanha")

print("Após adicionar a Espanha")
print(paises)

paises.remove("Portugal")

print("Após remoção do país Portugal")
print(paises)

paises.pop(2)

print("Após a remoção da Argentina")
print(paises)

print("Tamanho atual da lista de países")
print(len(paises))