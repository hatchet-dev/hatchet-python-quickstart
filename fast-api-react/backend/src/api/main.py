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
def message(data: MessageRequest):

    messageId = hatchet.client.admin.run_workflow("GenerateWorkflow", {
        "request": data.model_dump()
    })

    # save step message id -> workflowRunId

    return {"workflowRunId": messageId}


def event_stream_generator(workflowRunId):
    stream = hatchet.client.listener.stream(workflowRunId)

    for event in stream:
        data = json.dumps({
            "type": event.type,
            "payload": event.payload,
            "workflowRunId": workflowRunId
        })
        yield "data: " + data + "\n\n"


@app.get("/stream/{messageId}")
async def stream(messageId: str):
    # message id -> workflowRunId
    workflowRunId = messageId
    return StreamingResponse(event_stream_generator(workflowRunId), media_type='text/event-stream')


def start():
    """Launched with `poetry run api` at root level"""
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
