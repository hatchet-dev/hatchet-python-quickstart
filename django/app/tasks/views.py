# tasks/views.py
from django.shortcuts import render
from django.http import JsonResponse, request
from django.views.decorators.http import require_http_methods
from hatchet.worker import hatchet

def index(request):
    return render(request, 'index.html')

@require_http_methods(["POST"])
def trigger_workflow(request: request.HttpRequest):
    message = request.POST.get('message', '')
    input = {"message": message}

    workflow_run = hatchet.event.push(
        event_key="django-example-event",
        payload=input,
    )

    return JsonResponse({
        "workflow_id": workflow_run.eventId,
    })
