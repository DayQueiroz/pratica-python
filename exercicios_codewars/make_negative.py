# Nesta tarefa simples, você recebe um número e precisa torná-lo negativo.  
# Mas talvez o número já seja negativo?


def make_negative( number ):
    if number > 0:
        return (number * -1)

    return (number)

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))

# escrita mais formal e enxuta
def make_negative(number):
    return number * -1 if number > 0 else number

# Sem usar if/else
def make_negative(number):
    return -abs(number)
# abs(number) - sempre transforma em positivo, quando coloca - na frente ele trasforme o numero
# em negativo