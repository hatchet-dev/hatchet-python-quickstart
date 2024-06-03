import asyncio
from src.hatchet import hatchet


@hatchet.workflow(on_events=["man:create"])
class ManualTriggerWorkflow:
    @hatchet.step()
    async def step1(self, context):
        res = context.playground('res', "HELLO")

        await asyncio.sleep(3)
        print("executed step1")
        return {"step1": "data1 "+res}

    @hatchet.step(parents=["step1"], timeout='4s')
    async def step2(self, context):
        print("started step2")
        await asyncio.sleep(1)
        print("finished step2")
        return {"step2": "data2"}
