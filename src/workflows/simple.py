from hatchet_sdk import Context, EmptyModel, Hatchet
from ..hatchet_client import hatchet

# Define the workflow
simple = hatchet.workflow(name="SimpleWorkflow")

# Declare the task to run
@simple.task()
def step1(input: EmptyModel, ctx: Context) -> None:
    print("executed step1")
