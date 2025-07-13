
from typing import Optional, Protocol


class CarroInterface(Protocol):
  marca: str
  modelo: str
  ano: Optional[int]
  ligado: bool

  def exibir_info(self) -> None: ...
  def ligar(self) -> None: ...
  def desligar(self) -> None: ...