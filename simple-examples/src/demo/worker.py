import logging
import time

from dotenv import load_dotenv

from hatchet_sdk import Context, Hatchet
from hatchet_sdk.loader import ClientConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

hatchet = Hatchet(
    debug=True,
    config=ClientConfig(
        logger=logging.getLogger(),
    ),
)


@hatchet.workflow(on_events=["demo:create"], schedule_timeout="10m")
class ExampleDagWorkflow:
    @hatchet.step(timeout="5s")
    def capitalize(self, context: Context):
        input: str = context.workflow_input()['input']

        logger.info(f"executed step1 - {input}")
        time.sleep(3)

        capitalized_output = input.capitalize()
        logger.info(f"Capitalized output: {capitalized_output}")

        return {
            "output": capitalized_output,
        }

    @hatchet.step()
    def lowercase(self, context: Context):
        input: str = context.workflow_input()['input']

        logger.info(f"executed step2 - {input}")
        time.sleep(5)

        lowercase_output = input.lower()
        logger.info(f"Lowercase output: {lowercase_output}")

        return {
            "output": lowercase_output,
        }

    @hatchet.step(parents=["capitalize", "lowercase"])
    def concat(self, context: Context):
        capitalized_output = context.step_output("capitalize")['output']
        lowercase_output = context.step_output("lowercase")['output']

        logger.info(f"executed step3 - Capitalized: {capitalized_output}, Lowercase: {lowercase_output}")
        time.sleep(3)

        concatenated_output = capitalized_output + lowercase_output
        logger.info(f"Concatenated output: {concatenated_output}")

        return {
            "output": concatenated_output,
        }

    @hatchet.step(parents=["concat"])
    def reverse(self, context: Context):
        concatenated_output = context.step_output("concat")['output']

        logger.info(f"executed step4 - Concatenated: {concatenated_output}")
        time.sleep(2)

        reversed_output = concatenated_output[::-1]
        logger.info(f"Reversed output: {reversed_output}")

        return {
            "output": reversed_output,
        }


workflow = ExampleDagWorkflow()
worker = hatchet.worker("demo-worker")
worker.register_workflow(workflow)

worker.start()
