from hatchet_sdk import Context
from ..hatchet import hatchet


@hatchet.workflow(on_events=["simple:create"])
class SimpleWorkflow:

    @hatchet.step()
    def step1(self, context: Context):
        test = context.playground("test", "test")
        test2 = context.playground("test2", 100)
        test3 = context.playground("test3", None)

        print(test)
        print(test2)

        print("executed step1")
        pass

    @hatchet.step(parents=["step1"], timeout='4s')
    def step2(self, context):
        print("started step2")
        context.sleep(1)
        print("finished step2")
