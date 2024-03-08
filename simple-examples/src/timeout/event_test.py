from src.hatchet import hatchet

hatchet.client.event.push(
    "timeout:create",
    {
        "test": "test"
    }
)
