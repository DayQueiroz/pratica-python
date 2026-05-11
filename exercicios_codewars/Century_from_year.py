# O primeiro século vai do ano 1 até o ano 100, inclusive; o segundo século, do ano 101 até o ano 200,
# inclusive; e assim por diante.
# Tarefa: Dado um ano, indique o século em que ele se encontra.

# 1. Receber o ano.
# 2. Verificar se o ano é multiplo de 100.
# 3. Se for: dividir o ano por 100 para achar o seculo
# 4. Se não for: dividir o ano por 100 com // para ter resultado inteiro e somar + 1



def century(year):
    if year % 100 == 0:  
        return year // 100
    else:
        return year // 100 + 1

year_input = 1705
print(century(year_input))
year_input = 1900
print(century(year_input))
year_input = 1601
print(century(year_input))
year_input = 2000
print(century(year_input))
year_input = 3458
print(century(year_input))
year_input = 2742

print(century(year_input))