from .hatchet import hatchet
from .simple.worker import SimpleWorkflow
from .concurrency_limit.worker import ConcurrencyDemoWorkflow
from .dag.worker import DagWorkflow
from .manual_trigger.worker import ManualTriggerWorkflow
from .timeout.worker import TimeoutWorkflow


from .genai.basicrag import BasicRagWorkflow
from .genai.simple import SimpleGenAiWorkflow


# This is the entry point for the Hatchet worker process
def start():
    worker = hatchet.worker('example-worker')

    # Instantiate the workflow and Register the workflow with the worker
    worker.register_workflow(SimpleWorkflow())
    worker.register_workflow(ConcurrencyDemoWorkflow())
    worker.register_workflow(DagWorkflow())
    worker.register_workflow(ManualTriggerWorkflow())
    worker.register_workflow(TimeoutWorkflow())

    # Generative AI Examples
    worker.register_workflow(BasicRagWorkflow())
    worker.register_workflow(SimpleGenAiWorkflow())

    # Start the worker and begin listening for events
    worker.start()
