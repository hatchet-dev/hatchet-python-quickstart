import asyncio
from hatchet_sdk import Context
from src.hatchet import hatchet


@hatchet.workflow(on_events=["timeout:create"])
class TimeoutWorkflow:

    @hatchet.step(timeout='4s')
    async def step1(self, context):
        try:
            print("started step2")
            await asyncio.sleep(5)
            print("finished step2")
        except Exception as e:
            print("caught an exception: " + str(e))
            raise e
