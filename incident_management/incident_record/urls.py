from django.urls import path
from .views import (
    IncidentListView,
    IncidentCreateView,
    IncidentUpdateView,
    IncidentDeleteView,
)

app_name = "incident_record"
urlpatterns = [
    path("list/", IncidentListView.as_view(), name="incident-list"),
    path("incident-create/", IncidentCreateView.as_view(), name="incident-create"),
    path("<int:id>", IncidentUpdateView.as_view(), name="incident-update"),
    path("<int:id>/delete", IncidentDeleteView.as_view(), name="incident-delete"),
]
