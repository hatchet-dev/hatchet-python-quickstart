## Hatchet Python Quickstart

The following is a template repo to get started with the Hatchet Python SDK. It includes instructions for getting started with Hatchet cloud along with a locally running instance of Hatchet.

### Cloud Version

Navigate to your settings tab in the Hatchet dashboard. You should see a section called "API Keys". Click "Create API Key", input a name for the key and copy the key. Then set the following environment variables:

```
HATCHET_CLIENT_TOKEN="<token>"
```

Then start a worker via:

```
poetry run python worker.py
```

**Next steps:** see [Running Workflows](#running-workflows) to trigger your first Hatchet workflow.

### Local Version

Run the following command to start the Hatchet instance:

```
docker compose up
```

This will start a Hatchet instance on port `8080`. You should be able to navigate to [localhost:8080](localhost:8080) and use the following credentials to log in:

```
Email: admin@example.com
Password: Admin123!!
```

Next, navigate to your settings tab in the Hatchet dashboard. You should see a section called "API Keys". Click "Create API Key", input a name for the key and copy the key. Then set the following environment variables:

```
HATCHET_CLIENT_TOKEN="<token>"
```

**Next steps:** see [Running Workflows](#running-workflows) to trigger your first Hatchet workflow.

## Running Workflows

## Using the Playground
