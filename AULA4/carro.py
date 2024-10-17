import veiculo 

class Carro(veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, num_portas):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.num_portas = num_portas

    def calcular_aluguel(self, dias):
        valor = super().calcular_aluguel(dias)
        if dias > 7:
            valor *=0.90
        self.listar_veiculo()
        print(f"Valor aluguel de {dias} dias = {valor}")