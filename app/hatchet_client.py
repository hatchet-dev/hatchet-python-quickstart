from hatchet_sdk import ClientConfig, Hatchet

from app.config import settings

hatchet = Hatchet(
    config=ClientConfig(
        token=settings.HATCHET_CLIENT_TOKEN,
        host_port=settings.HATCHET_CLIENT_HOST_PORT,
    )
)
