# Hatchet FastAPI Example

This is an example project demonstrating how to run a simple Hatchet worker.

## Prerequisites

Before running this project, make sure you have the following:

1. Python 3.7 or higher installed on your machine.
2. Poetry package manager installed. You can install it by running `pip install poetry`, or by following instructions in the [Poetry Docs](https://python-poetry.org/docs/#installation)

## Setup

1. Create a `.env` file in this directory and set the required environment variables. This requires the `HATCHET_CLIENT_TOKEN` variable created in the [Getting Started README](/README.md).

```
HATCHET_CLIENT_TLS_STRATEGY=none
HATCHET_CLIENT_TOKEN="<token>"
```

2. Open a terminal and navigate to the project root directory (`/simple-examples`).

3. Run the following command to install the project dependencies:

   ```shell
   poetry install
   ```

## Running the Hatchet Worker

In a separate terminal, start the the Hatchet worker by running the following command:

```shell
poetry run hatchet
```

You can then navigate to the workflow in the Hatchet dashboard to view the structure of this workflow.
