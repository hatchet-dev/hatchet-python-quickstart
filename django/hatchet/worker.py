from hatchet_sdk import Hatchet, Context

hatchet = Hatchet(debug=True)

@hatchet.workflow(on_events=["django-example-event"])
class DjangoExampleWorkflow:
    @hatchet.step()
    def example_step(self, ctx: Context) -> None:
        workflow_input = ctx.workflow_input()

        print(f"Received message: {workflow_input['message']}")

if __name__ == "__main__":
    worker = hatchet.worker(name="django-example-worker")
    worker.register_workflow(DjangoExampleWorkflow())
    worker.start()

