from datetime import datetime, timedelta

# Classe Caminhão
class Caminhao:
    def __init__(self, modelo, placa, capacidade_carga):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.carga_atual = 0  # Atributo adicional para controlar a carga atual
        self.motorista = None

    def carregar(self, peso):
        if self.carga_atual + peso <= self.capacidade_carga:
            self.carga_atual += peso
            print(f'{peso} kg carregados no caminhão {self.modelo}. Carga atual: {self.carga_atual} kg.')
        else:
            print(f'Erro: o peso excede a capacidade do caminhão {self.modelo}.')

    def descarregar(self, peso):
        if peso <= self.carga_atual:
            self.carga_atual -= peso
            print(f'{peso} kg descarregados do caminhão {self.modelo}. Carga atual: {self.carga_atual} kg.')
        else:
            print(f'Erro: não há carga suficiente para descarregar.')

# Classe Motorista
class Motorista:
    def __init__(self, nome, idade, CNH, dataValidade):
        self.nome = nome
        self.idade = idade
        self.CNH = CNH
        self.dataValidade = dataValidade
        self.caminhoes = []  # Lista de caminhões que o motorista dirige

    def dirigir(self, caminhao):
        if self.verificarValidade():
            caminhao.motorista = self
            self.caminhoes.append(caminhao)
            print(f'{self.nome} está dirigindo o caminhão {caminhao.modelo}.')
        else:
            print(f'{self.nome} não pode dirigir. CNH vencida ou prestes a vencer.')

    def verificarValidade(self):
        hoje = datetime.now().date()
        if self.dataValidade < hoje:
            print(f'A CNH de {self.nome} está vencida.')
            return False
        elif self.dataValidade <= hoje + timedelta(days=30):
            print(f'A CNH de {self.nome} vence em breve. Por favor, renove.')
        return True

# Função para calcular o frete
def calcular_frete(distancia, peso):
    taxa_por_km = 2.0  # Exemplo de taxa por km
    taxa_por_kg = 0.05  # Exemplo de taxa por kg
    frete = (distancia * taxa_por_km) + (peso * taxa_por_kg)
    return frete

# Classe Viagem
class Viagem:
    def __init__(self, caminhao, distancia, carga):
        self.caminhao = caminhao
        self.distancia = distancia
        self.carga = carga
        self.frete = calcular_frete(distancia, carga)

    def info_viagem(self):
        print(f'Caminhão: {self.caminhao.modelo}, Placa: {self.caminhao.placa}')
        print(f'Distância: {self.distancia} km, Carga transportada: {self.carga} kg')
        print(f'Frete calculado: R${self.frete:.2f}')

# Criando 3 objetos da classe Caminhão
caminhao1 = Caminhao("Mercedes Benz", "AAA-1234", 10000)
caminhao2 = Caminhao("Volvo FH", "BBB-5678", 8000)
caminhao3 = Caminhao("Scania R450", "CCC-9876", 12000)

# Criando 2 objetos da classe Motorista
motorista1 = Motorista("João Silva", 45, "123456789", datetime(2024, 10, 15).date())
motorista2 = Motorista("Carlos Souza", 50, "987654321", datetime(2023, 9, 30).date())

# Atribuindo motoristas aos caminhões
motorista1.dirigir(caminhao1)
motorista1.dirigir(caminhao2)
motorista2.dirigir(caminhao3)

# Simulando carga e descarga
caminhao1.carregar(5000)
caminhao1.descarregar(2000)

# Verificando validade da CNH
motorista2.verificarValidade()

# Criando uma viagem e calculando o frete
viagem1 = Viagem(caminhao1, 500, caminhao1.carga_atual)
viagem1.info_viagem()

# Imprimindo informações sobre os caminhões e motoristas
def imprimir_info(caminhao):
    print(f'Caminhão:')
    print(f'  Modelo: {caminhao.modelo}')
    print(f'  Placa: {caminhao.placa}')
    print(f'  Capacidade de carga: {caminhao.capacidade_carga} kg')
    print(f'  Motorista: {caminhao.motorista.nome if caminhao.motorista else "Sem motorista"}')
    print(f'  Carga atual: {caminhao.carga_atual} kg')

imprimir_info(caminhao1)
imprimir_info(caminhao2)
imprimir_info(caminhao3)
