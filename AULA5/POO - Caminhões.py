from datetime import datetime, timedelta

class Caminhão:
    def __init__(self, modelo, placa, capacidade_carga, motorista):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.motorista = motorista

    def carregar(self, peso):
        while True:
            self.carga_atual = peso
            if self.carga_atual > self.capacidade_carga:
                print("Peso inserido maior que o limite máximo!")
            else: 
                print("Limite máxima de carga excedido!")  

    def descarregar(self):
        self.carga_atual = self.capacidade_carga - self.carga_atual

    def Motora(self, motora):
        self.motorista = motora

class Motora:
    def __init__(self, nome, idade, cnh):
        self.nome = nome
        self.idade = idade
        self.cnh = cnh
        self.trucks = []

    def renovarCnh(self, cnh):
        data_atual = datetime.datetime.now
        renovacaoCnh = data_atual + relativedelta(year=5)
        self.cnh = self.cnh + renovacaoCnh

    def verificarValidade(self):
        data_atual = datetime.datetime.now
        one_month_later = data_atual + timedelta(days=30)
        if self.cnh < one_month_later:
            print("Cnh vencida ou a um mês para vencer! Renove-a imediatamente!")
            
        else:
            print("Cnh válida!")          


    def adicionarCaminhao(self, truck):
        self.trucks.append(truck)
        truck.definirMotora(self)