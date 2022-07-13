from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    PROJECT_NAME: str = "Todo API"

    # Database settings
    DB_URL: str = "sqlite:///database.db"


settings = BaseSettings()
