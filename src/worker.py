from hatchet_client import hatchet
from workflows.simple import simple

def main() -> None:
    worker = hatchet.worker(
        "test-worker", 
        slots=1, 
        workflows=[simple]
    )
    worker.start()

if __name__ == "__main__":
    main()
