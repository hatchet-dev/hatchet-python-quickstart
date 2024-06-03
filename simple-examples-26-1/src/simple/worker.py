import asyncio
from hatchet_sdk import Context
from src.hatchet import hatchet

@hatchet.workflow(on_events=["simple:create"])
class SimpleWorkflow:

    @hatchet.step()
    def step1(self, context: Context):
        print(context.workflow_input())
        context.log('hello world')
        print("executed step1")
        pass

    @hatchet.step(parents=["step1"], timeout='4s')
    async def step2(self, context):
        print("started step2")
        await asyncio.sleep(1)
        print("finished step2")