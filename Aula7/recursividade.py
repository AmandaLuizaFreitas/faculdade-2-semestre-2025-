# funções recursivas na linguagem Python

# def calcular(n1):
#     return calcular(n1 - 1)
# print(calcular(78))

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
print(fatorial(5))