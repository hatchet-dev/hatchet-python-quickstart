from .hatchet import hatchet
from hatchet_sdk import Context
import openai


@hatchet.workflow()
class SimpleWorkflow:
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
