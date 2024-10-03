from animal import Animal

class Gato(Animal):
  def __init__(self, nome, idade, cor):
    super().__init__(nome, idade)
    self.cor = cor

  def emitir_som(self):
    print(f"{self.nome} está miando!")