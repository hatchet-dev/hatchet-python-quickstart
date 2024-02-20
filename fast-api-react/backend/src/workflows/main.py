from .hatchet import hatchet
from .generate import GenerateWorkflow, SimpleWorkflow


def start():
    worker = hatchet.worker('example-worker')

    generate = GenerateWorkflow()
    worker.register_workflow(generate)
    worker.register_workflow(SimpleWorkflow())

    worker.start()
