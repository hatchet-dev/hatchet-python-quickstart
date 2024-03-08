from src.hatchet import hatchet
from hatchet_sdk import Context
import openai

# This is a simple example of a workflow that uses the OpenAI GPT-3 model to generate an answer to a question.
# The workflow is declared decorated with `@hatchet_workflow` and the steps are declared with `@hatchet_step`.


@hatchet.workflow()
class SimpleGenAiWorkflow:
    @hatchet.step()
    def start(self, ctx: Context):
        message = ctx.workflow_input()["messages"][-1]

        prompt = ctx.playground(
            "prompt", "The user is asking the following question: {message}")

        prompt = prompt.format(message=message['content'])

        model = ctx.playground("model", "gpt-3.5-turbo")

        completion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                message
            ]
        )

        return {
            "answer": completion.choices[0].message.content,
        }
