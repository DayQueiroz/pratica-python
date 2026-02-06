esta_de_ferias = False
comprou_passagens = True

consegue_viajar = (esta_de_ferias and comprou_passagens)

print(f"Vai conseguir viajar? {consegue_viajar}")


nome_na_lista = False
tem_convite = False

entra_no_evento = (nome_na_lista or tem_convite)
print(f"Vai conseguir entrar no envento? {entra_no_evento}")