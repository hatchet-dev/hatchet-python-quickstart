from app.hatchet_client import hatchet
from app.workflows.first_workflow import my_task


def main() -> None:
    worker = hatchet.worker("test-worker", slots=1, workflows=[my_task])
    worker.start()


if __name__ == "__main__":
    main()
