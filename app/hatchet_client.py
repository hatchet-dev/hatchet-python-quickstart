from hatchet_sdk import ClientConfig, Hatchet

from app.config import settings

config_params = {
    "token": settings.HATCHET_CLIENT_TOKEN,
}

if settings.HATCHET_CLIENT_HOST_PORT:
    config_params["host_port"] = settings.HATCHET_CLIENT_HOST_PORT

hatchet = Hatchet(config=ClientConfig(**config_params))
