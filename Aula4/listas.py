# Lista & Matrizes 
# Array
numeros = [10,20,30,17]
print(numeros[0])

carros = ['Pálio', 'Gol', 'Virtus', 'Ka', 'Onix']
# print(carros[3])
# print(len(carros))

# carros.append('Kombi')
# print(carros)

print('1->', carros)
carros.append('Kombi')
print('2->',carros)
carros.remove('Gol')
print('3->',carros)

del carros[3]
print('4->',carros)

carros = sorted(carros)
print('5->',carros)

for i in carros:
    print(i)