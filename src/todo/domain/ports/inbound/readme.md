Aqui criamos as portas (interfaces) de entrada no core da aplicação.

No exemplo, abaixo uma porta para criação de uma revendedora.


```
from typing import Protocol, Optional
from domain.entities.reseller import Reseller


class CreateResellerInterface(Protocol):
    def create_reseller(self, email: str) -> Reseller:
        ...


```