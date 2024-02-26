## Hatchet Python Quickstart

The following is a template repo to get started with the Hatchet Python SDK. It includes instructions for getting started with Hatchet cloud along with a locally running instance of Hatchet.

### Cloud Version

Navigate to your settings tab in the Hatchet dashboard. You should see a section called "API Keys". Click "Create API Key", input a name for the key and copy the key. Then copy the environment variable:

```
HATCHET_CLIENT_TOKEN="<token>"
```

You will need this in the examples.

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

Next, navigate to your settings tab in the Hatchet dashboard. You should see a section called "API Keys". Click "Create API Key", input a name for the key and copy the key. Then copy the environment variable:

```
HATCHET_CLIENT_TOKEN="<token>"
```

You will need this in the examples.

**Next steps:** see [Running Workflows](#running-workflows) to trigger your first Hatchet workflow.

## Running Workflows

This repository includes two example projects:

1. [fast-api and react](/fast-api-react): a full stack demo OpenAi chat application
2. [simple-examples](/simple-examples): stand-alone workers showing off core functionality of hatchet

To get started, navigate to the respective example directories for further README instructions and refer to the [Documentation](https://docs.hatchet.run/home/python-sdk/setup)

