Aqui criamos nossas portas outbound, como por exemplo de um repository ou de acesso a uma API externa.

Exemplo de interface:

```
from typing import Protocol, Optional
from domain.entities.reseller import Reseller


class ResellerRepositoryInterface(ABC):
    def get_by_id(self, reseller_id: str) -> Cart:
        ...

    @abstractmethod
    def save(self, cart: Cart) -> bool:
        ...

    @abstractmethod
    def delete(self, cart_id: str) -> bool:
        ...

```