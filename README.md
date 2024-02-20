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

To get started, navigate to the respective example directories for further README instructions.

## Using the Playground

The Playground is a powerful feature within the Hatchet environment that allows you to experiment, develop, and test workflows interactively before deploying them into production. It is designed to offer a user-friendly interface where you can write, edit, and execute code steps that live within your code, as well as simulate and debug your workflows in a controlled setting. Here's how to get started:

### Accessing the Playground

1. **Sign In**: First, sign into your Hatchet dashboard.
2. **Navigate to Workflows**: Look for the "Workflow" section in the navigation menu on the left side of your screen. Clicking this will display a list of your registered workflows.
3. **Interact with Workflows**: Choose a workflow to explore. Then, select one of its runs to examine and interact with the inputs and outputs of specific steps within that workflow.

#### Features and How to Use Them

##### Input/Output View

- **Step Interaction**: Each step in a workflow is presented with a distinct input form and an output section for your review.
- **Modifying Step Inputs**: You have the capability to adjust various components of a step's input:

###### Workflow Input

This is the initial data that triggers the workflow. You can modify this to test how different inputs affect the workflow.

###### Parent Data

These are the outputs from preceding steps in the workflow. You can view and modify these to understand how data flows through and affects subsequent steps.

###### Playground

Within each step of your workflow, there is a `context` parameter. This parameter features a unique method called `playground`, which accepts two arguments: a name (as a string) and a value (which must be a primitive data type). This functionality is designed to dynamically adjust certain aspects of your workflow on the fly. When you execute a step in the Playground, Hatchet recognizes any `playground` you've implemented, enabling you to modify them directly. This flexibility is especially useful for fine-tuning specific parameters, such as adjusting prompt instructions or other configurations.

###### Debugging

- **Error Identification and Resolution**: The Playground is equipped with debugging tools aimed at efficiently identifying and resolving errors within your workflows. It displays error messages and logs in the output section, providing clear insights into issues that need attention.
- **Event Replay**: A future feature will allow for the replay of events within your local development environment. This means you'll be able to revisit specific events, make necessary code adjustments, and verify that errors have been effectively addressed, further enhancing the debugging process.
