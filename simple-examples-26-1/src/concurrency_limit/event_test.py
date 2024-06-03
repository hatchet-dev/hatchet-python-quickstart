from src.hatchet import hatchet

hatchet.client.event.push(
    "concurrency-test",
    {
        "test": "test"
    }
)
