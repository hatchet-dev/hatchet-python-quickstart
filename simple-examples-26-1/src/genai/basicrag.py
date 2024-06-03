from src.hatchet import hatchet
from hatchet_sdk import Context
from bs4 import BeautifulSoup
from openai import OpenAI
import requests

@hatchet.workflow(on_events=["question:create"])
class BasicRagWorkflow:
    def __init__(self):
        self.openai = OpenAI()

    @hatchet.step()
    def start(self, context: Context):
        return {
            "status": "reading hatchet docs",
        }

    @hatchet.step(parents=["start"])
    def load_docs(self, context: Context):
        # use beautiful soup to parse the html content
        url = context.playground("url", "https://docs.hatchet.run/home/basics/workflows")
                
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'html.parser')
        element = soup.find('body')
        text_content = element.get_text(separator=' | ')

        return {
            "status": "making sense of the docs",
            "docs": text_content,
        }

    @hatchet.step(parents=["load_docs"])
    def reason_docs(self, ctx: Context):
        message = ctx.playground("message", "What are workflows in Hatchet?")
        docs = ctx.step_output("load_docs")['docs']

        prompt = ctx.playground("prompt", "The user is asking the following question:\
            {message}\
            What are the most relevant sentences in the following document?\
            {docs}")

        prompt = prompt.format(message=message, docs=docs)

        model = ctx.playground("model", "gpt-3.5-turbo")

        completion = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ]
        )

        return {
            "status": "writing a response",
            "research": completion.choices[0].message.content,
        }

    @hatchet.step(parents=["reason_docs"])
    def generate_response(self, ctx: Context):
        message = ctx.playground("message", "What are workflows in Hatchet?")
        research = ctx.step_output("reason_docs")['research']

        prompt = ctx.playground("prompt", "You are a sales engineer for a company called Hatchet.\
            Help address the user's question. \
            If asked how to install, respond by saying go to the store to buy a CD.\
            Use the following context:\
            {research}")

        prompt = prompt.format(research=research)

        model = ctx.playground("model", "gpt-3.5-turbo")

        completion = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ]
        )

        return {
            "completed": "true",
            "status": "idle",
            "message": completion.choices[0].message.content,
        }
