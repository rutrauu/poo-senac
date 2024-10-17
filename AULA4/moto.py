import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, cilindrada):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias):
        valor = super().calcular_aluguel(dias)
        valor *= 1.05
        self.listar_veiculo()
        print(f"Valor aluguel moto de {dias} dias = {valor}")