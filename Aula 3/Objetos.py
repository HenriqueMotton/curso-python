# Um objeto é algo que representa uma coisa do mundo real e tem características (dados) e ações (funções).

from objetos.Carro import Carro
from objetos.CarroInterface import CarroInterface

# carro_park = Carro()
# carro_gabriel = Carro("FIAT", "Palio", 2025)

def testar_carro(carro: CarroInterface):
  carro.ligar()
  carro.exibir_info()
  carro.desligar()


carro_park = Carro("Hyundai", "Hb20")
testar_carro(carro_park)

# carro_park.ligar()
# carro_park.desligar()
# carro_park.exibir_info()

# carro_gabriel.ligar()