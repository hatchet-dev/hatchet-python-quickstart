from src.hatchet import hatchet


hatchet.client.event.push(
    "user:create",
    {
        "test": "test"
    }
)
