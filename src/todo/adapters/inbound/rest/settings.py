from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    todo: str = "Cart API"


settings = BaseSettings()
