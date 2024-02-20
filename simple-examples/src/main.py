from .hatchet import hatchet
from .simple import SimpleWorkflow

# This is the entry point for the Hatchet worker process


def start():
    worker = hatchet.worker('example-worker')

    # Instantiate the workflow and Register the workflow with the worker
    simple = SimpleWorkflow()
    worker.register_workflow(simple)

    # Start the worker and begin listening for events
    worker.start()
