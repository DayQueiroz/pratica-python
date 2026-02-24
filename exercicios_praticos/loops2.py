limite = int(input("Informe o limite"))
produtorio = 1      #produtorio é a multiplicação dos numeros

for i in range(1, limite + 1):
    produtorio = produtorio * i

print(f"Resultado produtório: {produtorio}")