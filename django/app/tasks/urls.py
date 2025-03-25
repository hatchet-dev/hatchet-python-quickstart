from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trigger-workflow/', views.trigger_workflow, name='trigger_workflow'),
]