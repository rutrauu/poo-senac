class Veiculo:
    def __init__(self, marca, modelo, ano, preco_diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria

    def calcular_aluguel(self, dias):
        return self.preco_diaria * dias

    def listar_veiculo(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)
        print(self.preco_diaria)

        

        