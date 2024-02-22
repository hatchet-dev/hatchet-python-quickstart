from .hatchet import hatchet
from .basicrag import BasicRagWorkflow
from .simple import SimpleWorkflow


def start():
    worker = hatchet.worker('example-worker')

    worker.register_workflow(BasicRagWorkflow())
    worker.register_workflow(SimpleWorkflow())

    worker.start()
