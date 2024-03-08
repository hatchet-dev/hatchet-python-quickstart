from src.hatchet import hatchet

workflowRunId = hatchet.client.admin.run_workflow("ManualTriggerWorkflow", {
    "test": "test"
})

hatchet.client.listener.on(workflowRunId, lambda event: print(
    'EVENT: ' + event.type + ' ' + json.dumps(event.payload)))
