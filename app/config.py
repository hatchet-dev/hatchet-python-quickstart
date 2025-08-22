from typing import Literal, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ref:https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    HATCHET_CLIENT_TOKEN: str
    HATCHET_CLIENT_HOST_PORT: Optional[str] = None


settings = Settings()  # type: ignore
