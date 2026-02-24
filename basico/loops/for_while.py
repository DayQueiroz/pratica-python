for i in range(1, 6):  # i = [1,2,3,4,5] por regra o utimo numero [6] não entra na execução do indice
    print(i)


senha = input("Informe a senha: ")

while senha != 'cdc2025':
    print("Senha incorreta! Tente novamente")
    senha = input("Informe a senha: ")

print("Senha correta. Fim do while")


# em caso de loop infinito para parar a execução do terminar utilizar o atalho ctrol+c