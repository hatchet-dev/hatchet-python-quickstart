import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
from dotenv import load_dotenv
import json

from hatchet_sdk import Hatchet

from .models import MessageRequest


load_dotenv()

app = FastAPI()

hatchet = Hatchet()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/message")
async def message(data: MessageRequest):
    ''' This endpoint is called by the client to start a message generation workflow. '''
    workflowRun = await hatchet.client.admin.aio.run_workflow("BasicRagWorkflow", {
        "request": data.model_dump()
    })

    # normally, we'd save the workflow_run_id to a database and return a reference to the client
    # for this simple example, we just return the workflow_run_id

    return {"messageId": workflowRun.workflow_run_id}

async def event_stream_generator(workflowRunId):
    ''' This helper function is a generator that yields events from the Hatchet event stream. '''
    workflowRun = hatchet.client.admin.get_workflow_run(workflowRunId)

    async for event in workflowRun.stream():
        ''' you can filter and transform event data here that will be sent to the client'''
        data = json.dumps({
            "type": event.type,
            "payload": event.payload,
            "messageId": workflowRunId
        })
        yield "data: " + data + "\n\n"

    result = await workflowRun.result()

    data = json.dumps({
        "type": "result",
        "payload": result,
        "messageId": workflowRunId
    })

    yield "data: " + data + "\n\n"

@app.get("/message/{messageId}")
async def stream(messageId: str):
    '''
    in a normal application you might use the message id to look up a workflowRunId
    for this simple case, we have no persistence and just use the message id as the workflowRunId

    you might also consider looking up the workflowRunId in a database and returning the results if the message has already been processed
    '''
    workflowRunId = messageId
    return StreamingResponse(event_stream_generator(workflowRunId), media_type='text/event-stream')


def start():
    """Launched with `poetry run api` at root level"""
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
