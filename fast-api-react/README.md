# Hatchet FastAPI Example

This is an example project demonstrating how to use Hatchet with FastAPI.

## Prerequisites

Before running this project, make sure you have the following:

1. Python 3.10 or higher installed on your machine.
2. Poetry package manager installed. You can install it by running `pip install poetry`, or by following instructions in the [Poetry Docs](https://python-poetry.org/docs/#installation)
3. (Optional) If you would like to run the example frontend, Node which can be installed from the [node website](https://nodejs.org/en/download)

## Setup

1. Create a `.env` file in the `./backend` directory and set the required environment variables. This requires the `HATCHET_CLIENT_TOKEN` variable created in the [Getting Started README](../README.md). You will also need, a `OPENAI_API_KEY` which can be created on the [OpenAI Website](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

**If you're running Hatchet locally without TLS:**

```
HATCHET_CLIENT_TLS_STRATEGY=none
HATCHET_CLIENT_TOKEN="<token>"
OPENAI_API_KEY="<openai-key>"
```

**If you're using Hatchet Cloud:**

```
HATCHET_CLIENT_TOKEN="<token>"
OPENAI_API_KEY="<openai-key>"
```

2. Open a terminal and navigate to the project backend directory (`/fast-api-react/backend`).

3. Run the following command to install the project dependencies:

```shell
poetry install
```

### Running the API

To start the FastAPI server, run the following command in the terminal:

```shell
poetry run api
```

### Running the Hatchet Worker

In a separate terminal, start the the Hatchet worker by running the following command:

```shell
poetry run hatchet
```

### (Optional) Running the Example Frontend Application

We've included a basic chat engine frontend to play with the example workflow. To run this script:

1. Open a new terminal window and cd into the [`fast-api-react/frontend`](./frontend/) directory.
2. run `npm install`
3. run `npm start`
4. By default you can access the application in your browser at `http://localhost:3000` or by following the instructions in the terminal window.

## Project Overview

### Example Workflows

The project contains two example workflows in the [`./backend/src/workflows`](./backend/src/workflows/) directory. These workflows are registered with hatchet in [`./backend/src/workflows/main.py`](./backend/src/workflows/main.py) which is started when running `poetry run hatchet`.

1. [Simple Response Generation](./backend/src/workflows/simple.py): a single step workflow making a request to OpenAI
2. [Basic Retrieval Augmented Generation](./backend/src/workflows/basicrag.py): a multi-step workflow to load the contents of a website with Beautiful soup, reason about the information, and generate a response with OpenAI.

### Exposing the workflows via a RestAPI

A common design pattern is to start a Hatchet workflow run from a rest api endpoint. In this way, you can handle authentication and authorization as you normally do and let Hatchet handle execution. The simple FastAPI example can be found at [./backend/src/api/main.py](./backend/src/api/main.py)

### Starting a Run

The `POST /message` endpoint initiates a Hatchet workflow run, utilizing the message body as input. Given Hatchet operates asynchronously, this endpoint immediately returns a run ID. This ID acts as a reference for clients to track the status and outcomes of the initiated run.

### Streaming Responses

After initiating a workflow run and receiving a run ID, clients can subscribe to updates through a `GET /message/{id}` request. This request allows clients to receive real-time notifications and results from the asynchronous Hatchet worker, associated with their specific run ID.
