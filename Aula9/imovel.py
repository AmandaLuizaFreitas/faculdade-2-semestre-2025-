# Herança em python

class Imovel:
    def __init__(self, endereco, preco,nome,valor,area):
        self.endereco = endereco
        self.preco = preco
        self.nome = nome
        self.valor = valor
        self.area = area
        
    def detalhar(self):
       print(self)

    def calculorImposto(self):
           return self.valor * 0.03
            

Imovel1 = Imovel("Rua A, 123", 250000,"Casa",250000,120)
Imovel2 = Imovel("Av. B, 456", 150000,"Apartamento",150000,80)  



class ImovelComercial(Imovel):
    def __init__(self, endereco, preco,nome,valor,area,tipo_negocio):
        super().__init__(endereco, preco,nome,valor,area)
        self.tipo_negocio = tipo_negocio

    def calculorImposto(self):
           return self.valor * 0.05


Imovel3 = ImovelComercial("Rua C, 789", 500000,"Loja",500000,200,"Varejo")

print(Imovel3.__dict__)

# print(Imovel1.__dict__)
# print(Imovel2.__dict__)
# print("Imposto Imovel 1:", Imovel1.calculorImposto())
# print("Imposto Imovel 2:", Imovel2.calculorImposto())


# Herança Múltipla

class ImovelRural(Imovel):
    def __init__(self, endereco, preco,nome,valor,area,tipo_producao):
        super().__init__(endereco, preco,nome,valor,area)
        self.tipo_producao = tipo_producao

    def calculorImposto(self):
           return self.valor * 0.02 
    