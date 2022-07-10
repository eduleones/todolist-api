Em *Entity* criamos as entidades do nosso domínio.

Exemplo:

```
from typing import Optional
from pydantic import BaseModel


class Reseller(BaseModel):
    reseller_id: int
    email: str
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


```