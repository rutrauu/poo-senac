from gato import Gato
from cachorro import Cachorro
from passaro import Passaro

cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mia", 2, "Branco")
passaro = Passaro("Piu-Piu", 1, "Canario")

cachorro.emitir_som()
gato.emitir_som()
passaro.emitir_som()
