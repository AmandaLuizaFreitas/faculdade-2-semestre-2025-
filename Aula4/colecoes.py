# conjuntos

conjunto = set([4,7,8,8,0])
print("conjunto:",conjunto)
# tupla
tupla = (3,2,4,6,0)
print(tupla)

# dicionarios 

pessoa = ['Orion', 'Maria','João']
print(pessoa)

pessoa = {'nome':'José','telefone':'(99)99999-9999','endereco':'ABCD'}
print(pessoa['telefone'])

pessoa = [
    {'nome':'José','telefone':'(99)99999-9999','endereco':'ABCD'},
     {'nome':'João','telefone':'(99)99999-0999','endereco':'ABC'},
     {'nome':'Felipe','telefone':'(99)99199-0999','endereco':'ABF'}
]
print(pessoa[2]["tele"])