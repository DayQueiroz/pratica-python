dicionario = {
    "nome": "Dayana",
    "estado": "São Paulo",
    "altura": 1.65
} 

print(f"Tipo do dicionário: {type(dicionario)}")
print(dicionario)
print(dicionario["nome"])
print(dicionario["estado"])
print(dicionario["altura"])

dicionario["nome"] = "Maria"
print(dicionario)

# posso adicionar campo ao dicionáio, sem nenhum erro, pois o dicionário é altamente flexivel 
dicionario["linguagem"] = "Python"
print(dicionario)