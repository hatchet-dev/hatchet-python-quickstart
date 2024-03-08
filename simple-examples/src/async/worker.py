from hatchet_sdk import Context
from src.hatchet import hatchet
import asyncio


@hatchet.workflow(on_events=["async:create"])
class AsyncWorkflow:

    @hatchet.step()
    async def step1(self, context: Context):
        print("sleeping...")
        await asyncio.sleep(5)
        print("...done sleeping")

        return {"step1": "complete!"}


worker = hatchet.worker("example-worker")
worker.register_workflow(AsyncWorkflow())
worker.start()
