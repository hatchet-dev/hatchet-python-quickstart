from .hatchet import hatchet
from hatchet_sdk import Context

# This is a simple example of a workflow that has 3 steps.
# The workflow is declared decorated with `@hatchet_workflow` and the steps are declared with `@hatchet_step`.


@hatchet.workflow(on_events=["simple:create"])
class SimpleWorkflow:

    @hatchet.step()
    def step1(self, context: Context):

        # The context object is passed to each step and contains the input data for the workflow.
        messages = context.workflow_input()['request']['messages']
        print("> starting step1", messages)
        return {"status": "thinking"}

    @hatchet.step(parents=["step1"])
    def step2(self, context: Context):
        print("starting step2")
        return {"status": "writing a response"}

    @hatchet.step(parents=["step2"], timeout='5m')
    def step3(self, context: Context):
        messages = context.workflow_input()['request']['messages']
        return {"complete": "true", "status": "idle", "message": "response from step3"}
