from hatchet_sdk import Context
from src.hatchet import hatchet


@hatchet.workflow(on_events=["user:create"])
class DagWorkflow:

    @hatchet.step()
    def step1(self, context: Context):
        overrideValue = context.playground(
            "prompt", "You are an AI assistant...")

        print("executed step1", context.workflow_input())
        return {
            "step1": overrideValue,
        }

    @hatchet.step()
    def step2(self, context: Context):
        print("executed step2", context.workflow_input())
        return {
            "step2": "step2",
        }

    @hatchet.step(parents=["step1", "step2"])
    def step3(self, context: Context):
        print("executed step3", context.workflow_input(),
              context.step_output("step1"), context.step_output("step2"))
        return {
            "step3": "step3",
        }

    @hatchet.step(parents=["step1", "step3"])
    def step4(self, context: Context):
        print("executed step4", context.workflow_input(),
              context.step_output("step1"), context.step_output("step3"))
        return {
            "step4": "step4",
        }
