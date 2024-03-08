from hatchet_sdk import Context
from src.hatchet import hatchet


@hatchet.workflow(on_events=["simple:create"])
class SimpleWorkflowG:

    @hatchet.step()
    def step1(self, context: Context):
        print(context.workflow_input())
        context.log('hello world')
        print("executed step1")
        pass

    @hatchet.step(parents=["step1"], timeout='4s')
    def step2(self, context):
        print("started step2")
        context.sleep(1)
        print("finished step2")


worker = hatchet.worker("example-worker-g")
worker.register_workflow(SimpleWorkflowG())
worker.start()
