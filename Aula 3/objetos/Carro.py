from typing import Optional


class Carro:
  def __init__(self, marca, modelo, ano: Optional[int] = None):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.ligado = False

  def exibir_info(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Ano: {self.ano if self.ano else 'Não informado'}")
    print(f"Está ligado? { 'Sim' if self.ligado else 'Não' }")

  def ligar(self):
    if not self.ligado:
      self.ligado = True
      print(f"{self.modelo} está agora ligado.")
    else:
      print(f"{self.modelo} já está ligado.")

  def desligar(self):
    if self.ligado:
      self.ligado = False
      print(f"{self.modelo} foi desligado.")
    else:
      print(f"{self.modelo} já está desligado.")

