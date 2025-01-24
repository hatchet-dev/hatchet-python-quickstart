from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tasks/", include("tasks.urls")),
    path("admin/", admin.site.urls),
]