# Class
class Produto:
           def __init__(self,nome,marca,modelo,valor , quantidade=0):
               self.nome = ""
               self.marca = ""
               self.modelo = ""
               self.valor = ""
               self.quantidade = 0
        # def estoque(self, quantidade):
        #        self.quantidade += quantidade
        # def venda(self, quantidade):
        #        if quantidade <= self.quantidade:
        #            self.quantidade -= quantidade
        #        else:
        #            print("Estoque insuficiente")
                                             
        

Produto0 = Produto( "caneta","Bic","Cristal",1.50,5  )
# Produto0.nome = "Caneta"

Produto1 = Produto("lapis","Faber-Castell","Nº2",0.50,10 )
# Produto1.nome = "Lápis"
Produto2 = Produto("caderno","Tilibra","Universitário",15.00,3 )
# Produto2.nome = "Caderno"

print(Produto0.__dict__)
print(Produto1.__dict__)
print(Produto2.__dict__)
