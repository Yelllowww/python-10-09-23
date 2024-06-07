class Console:
    def __init__(self,modelo=0,idade=0,valor=0):
        self.modelo = modelo
        self.idade = idade
        self.valor = valor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self,novo_modelo):
        if type(novo_modelo) == str:
            self.modelo = novo_modelo
        else:
            print("Dados inconsistentes")
    def get_idade(self):
        return self.idade
    def set_idade(self,nova_idade):
        self.idade = nova_idade
    def get_valor(self):
        return self.valor
    def set_valor(self,novo_valor):
        self.valor = novo_valor
    def soma_console(self,console):
        soma = self.valor + console.get_valor()
        return soma
    def porc_valor(self,console_vl,console):
        if self.valor > console:
            porcentagem = (self.valor - console_vl / (self.valor)) * 100
            return (porcentagem,"% maior")
        else:
            porcentagem = (console_vl - self.valor / (console_vl)) * 100
            return (porcentagem,"% menor")
    def __str__(self):
        return (f"O modelo do console é:{self.modelo},sua idade é {self.idade} e seu preço é {self.valor}")

    if __name__ == '__main__':
        console1 = Console('Playstation 4',10,1500)
        console2 = Console('Xbox one',11)
        console3 = Console('Nintendo switch')
        print("Console 1:")
        print("Modelo:",console1.get_modelo())
        print("Idade:",console1.get_idade())
        print("Valor:",console1.get_valor())
        console1.set_valor()
        print("Novo valor:",console1.get_valor())
        print(f"O console 1 é {console1.porc_valor(console2)} que o console 2")
        print(console1.__str__())

        print("Console 2:")
        print("Modelo:",console2.get_modelo())
        print("Idade:",console2.get_idade())
        console2.set_idade()
        print("Nova idade:",console2.get_idade())
        print(console2.__str__())


        print("Console 3:")
        print("Modelo:",console3.get_modelo())
        console3.set_modelo()
        print("Novo modelo:",console3.get_modelo())
        print(console3.__str__())