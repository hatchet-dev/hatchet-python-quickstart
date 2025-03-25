# Hatchet Simple Examples

This is an example project demonstrating how to use Hatchet with Python.


## Prerequisites

Before running this project, make sure you have the following:

1. [Python V3.10 or higher](https://www.python.org/downloads/)

## Setup

1. Set the required environment variable `HATCHET_CLIENT_TOKEN` created in the [Getting Started Guide](https://docs.hatchet.run/home/hatchet-cloud-quickstart).

```
export HATCHET_CLIENT_TOKEN=<token>
```

2. Run the following command to install the project dependencies:

   ```shell
   poetry install
   ```

### Running an example

1. Start a Hatchet worker by running the following command:

```shell
poetry run python -m hatchet.worker
```

2. To run the example workflow, open a new terminal and run the following command:

```shell
poetry run python -m hatchet.run
```

This will trigger the workflow on the worker running in the first terminal and print the output to the the second terminal.