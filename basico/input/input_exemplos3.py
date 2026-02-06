nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
resultado = ((nota1 + nota2) / 2)

media_round = round(resultado, 1) 
# utiliza-se o round para arrendondar e chamar a quantidade de casas decimais 

print(f"A média das notas informadas é: {media_round}")
