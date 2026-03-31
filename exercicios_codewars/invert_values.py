# Dado um conjunto de números, retorne o inverso aditivo de cada um.
#  Cada número positivo se torna negativo e os negativos se tornam positivos.
# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# Você pode assumir que todos os valores são inteiros. Não modifique o array de entrada.

## 1. Recebo uma Lista de numeros inteiros;
## 2. Criar uma lista vazia;
## 3. Percorra a Lista com um For:
##      Mutiplicar o item por -1 para inverter o sinal (de positivo para negativo e de negativo para positivo)
##      utilizar o metodo append para armazenar o numero modificado na nova lista.
##      (Aqui o enunciado não quer que você modifique a lista, usando o if por exemplo, ele que que so troque o sinal)
## 3. Retorna a lista modificada.

def invert(lst):
    inverted_lst = []

    for i in lst:
        inverted_i = i * -1
        inverted_lst.append(inverted_i)

    return inverted_lst

input_list = [1, -2, 3, -4, 5]
print (invert(input_list))