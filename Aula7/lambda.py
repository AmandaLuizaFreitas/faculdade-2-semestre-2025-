# funções anônimas
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = []

# for n in numero:
#     resultado.append(n * 2)
# print(resultado)


# def multiplcar (n1):
#     return n1 * 2

# resultado= map(multiplcar, numero)
# resultado= map(n1 * 2, numero)
resultado = map(lambda n1: n1 * 2, numero)

print(numero,list(resultado))