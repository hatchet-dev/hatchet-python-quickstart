from .hatchet import hatchet
from .basicrag import BasicRagWorkflow


def start():
    worker = hatchet.worker('basic-rag-worker')
    worker.register_workflow(BasicRagWorkflow())
    worker.start()
