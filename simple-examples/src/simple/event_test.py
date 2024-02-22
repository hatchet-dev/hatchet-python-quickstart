from ..hatchet import hatchet

hatchet.client.event.push(
    "simple:create",
    {
        "test": "test"
    }
)
