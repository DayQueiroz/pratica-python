# Exercicio para encontrar a agulha no palheiro
# Escreva uma função findNeedle()- encontrar agulha - que receba uma array lista cheia de lixo, 
# mas que contenha um único elemento - "needle"- agulha.
# Após a sua função encontrar a agulha, ela deverá retornar uma mensagem (em formato de texto) que diga:
# " Found the needle at position " - Encontrei a agulha na posição
# seguido do índice/posição em que a agulha foi encontrada

# Quebrando o problema: Encontrar a palavra "needle" em uma lista com diversas palavras.
# 1: Receber uma lista;
# 2: Percorrer a lista com um for;
# 3: Se o elemento for "needle":
    # pegar a posição(índice)
    # Retornar a mensagem com a posição
# 4: Parar o Loop.


def find_needle(haystack):
    position = 0

    for i in haystack:
        if i == "needle":
            break
        
        position = position + 1
    
    return f"found the needle at position {position}"


input_list = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

print(find_needle(input_list))


# podemos utilizar tbm nesse exercicio o metodo index,
# onde ele vai nos trazer a posição em que encontro a palavra desejada.
# def find_needle(haystack):
    #return f'found the needle at position {haystack.index("needle")}'