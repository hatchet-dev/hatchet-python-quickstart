## Hatchet Python Quickstart

This is an example project demonstrating how to use Hatchet with Python. For detailed setup instructions, see the [Hatchet Setup Guide](https://docs.hatchet.run/home/setup).

## Prerequisites

Before running this project, make sure you have the following:

1. [Python v3.10 or higher](https://www.python.org/downloads/)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/) for dependency management

## Setup

1. Clone the repository:

```bash
git clone https://github.com/tamasbelinszky/hatchet-python-quickstart
cd hatchet-python-quickstart
```

2. Set the required environment variable `HATCHET_CLIENT_TOKEN` created in the [Getting Started Guide](https://docs.hatchet.run/home/hatchet-cloud-quickstart).

```bash
cp .env.example .env # Add HATCHET_CLIENT_TOKEN
```

> Note: If you're self hosting you may need to set `HATCHET_CLIENT_TLS_STRATEGY=none` to disable TLS

3. Install the project dependencies:

```bash
uv sync
```

### Running an example

1. Start a Hatchet worker by running the following command:

```shell
uv run app/worker.py
```

or with docker-compose

```shell
docker-compose up
```

2. To run the example workflow, open a new terminal and run the following command:

```shell
uv run python -m app.worker
```

or visit your hatchet dashboard and trigger the workflow manually

This will trigger the workflow on the worker running in the first terminal and print the output to the the second terminal.
