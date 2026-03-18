# Crie uma função que receba um número inteiro como argumento e retorne "Par" 
# para números pares ou "Ímpar" para números ímpares.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    
    return "Odd"


print (even_or_odd(10)) # no codewars não mandar essa linha somente a função

# outra forma de fazer a função:
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
