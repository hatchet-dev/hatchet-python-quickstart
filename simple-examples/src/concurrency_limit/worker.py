from src.hatchet import hatchet


@hatchet.workflow(on_events=["concurrency-test"])
class ConcurrencyDemoWorkflow:

    @hatchet.concurrency(max_runs=5)
    def concurrency(self, context) -> str:
        return "concurrency-key"

    @hatchet.step()
    def step1(self, context):
        print("executed step1")
        pass

    @hatchet.step(parents=["step1"], timeout='4s')
    def step2(self, context):
        print("started step2")
        context.sleep(1)
        print("finished step2")
