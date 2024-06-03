from src.hatchet import hatchet

hatchet.client.event.push(
    "async:create",
    {
        "test": "test"
    }
)
