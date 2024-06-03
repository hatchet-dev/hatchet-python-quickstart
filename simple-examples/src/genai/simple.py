from src.hatchet import hatchet
from hatchet_sdk import Context
from openai import OpenAI

# This is a simple example of a workflow that uses the OpenAI GPT-3 model to generate an answer to a question.
# The workflow is declared decorated with `@hatchet_workflow` and the steps are declared with `@hatchet_step`.

@hatchet.workflow()
class SimpleGenAiWorkflow:
    def __init__(self):
        self.openai = OpenAI()

    @hatchet.step()
    def start(self, ctx: Context):
        message = ctx.playground("message", "What is the capital of France?")

        prompt = ctx.playground(
            "prompt", "The user is asking the following question: {message}")

        prompt = prompt.format(message=message)

        model = ctx.playground("model", "gpt-3.5-turbo")

        completion = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ]
        )

        return {
            "answer": completion.choices[0].message.content,
        }
