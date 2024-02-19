# Hatchet FastAPI Example

This is an example project demonstrating how to use Hatchet with FastAPI.

## Prerequisites

Before running this project, make sure you have the following:

1. Python 3.7 or higher installed on your machine.
2. Poetry package manager installed. You can install it by running `pip install poetry`, or by following instructions in the [Poetry Docs](https://python-poetry.org/docs/#installation)
3. Clone this repository to your local machine.
4. (Optional) If you would like to run the example frontend, Node which can be installed from the [node website](https://nodejs.org/en/download)

## Setup

1. Create a `.env` file in the project root directory and set the required environment variables.

This project requires the `HATCHET_CLIENT_TOKEN` variable created in the [Getting Started Readme](/README.md).

You will also need, a `OPENAI_API_KEY` which can be created on the [OpenAI Website](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

2. Open a terminal and navigate to the project root directory (`/fast-api-react`).

3. Run the following command to install the project dependencies:

   ```shell
   poetry install
   ```

## Running the API

To start the FastAPI server, run the following command in the terminal:

```shell
poetry run api
```

## Running the Hatchet Worker

In a separate terminal, start the the Hatchet worker by running the following command:

```shell
poetry run hatchet
```

## (Optional) Running the Example Frontend Application

We've included a basic chat engine frontend to play with the example workflow. To run this script:

1. Open a new terminal window and cd into the `fast-api-react/frontend` directory.
2. run `npx install`
3. run `npx start`
4. By default you can access the application in your browser at `http://localhost:3000` or by following the instructions in the terminal window.
