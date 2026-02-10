usuario_correto = ("admin")
senha_correta = ("python2025")

usuario = input("Digite o seu usuário: ")
senha = input("Digite sua senha: ")


if (usuario == usuario_correto) and (senha == senha_correta):
    print("login bem sucedido!")
else:
    print("As credenciais estão incorretas.")