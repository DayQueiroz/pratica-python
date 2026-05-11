# Dado um vetor de números inteiros, sua solução deve encontrar o menor número inteiro.
# Por exemplo:
# Dada [34, 15, 88, 2]a sua solução, retornará2
# Dada [34, -345, -1, 100]a sua solução, retornará-345
# Para efeitos deste kata, pode assumir que o array fornecido não estará vazio.

# Recebe uma lista de numero inteiros positivos ou negativos;
# Para encontrar o menor numero da lista:
#   Percorrer item por item e verificar se o item atual é menor que o anterior;
#   Guardar o menor entre eles.
# Retornar o ultimo numero guardado na variavél quando terminar os itens da lista.

def find_smallest_int(list):
    smallest_number = list[0]  #a partir da posição vai guardar o numero menor

    for item in list:
        if item < smallest_number:
            smallest_number = item
    
    return smallest_number


# tem uma função no proprio python que faz tudo que o laço for fez nesse exercicio. Que é a função "min"
# ficaria assim:
# def findSmallestInt(list):
#   return min(list)

list_input = [34, 15, 88, 2, 10]
print(find_smallest_int(list_input))

list_input = [34, -345, -1, 100]
print(find_smallest_int(list_input))