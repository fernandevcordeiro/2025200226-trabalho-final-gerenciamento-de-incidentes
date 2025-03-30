from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import IncidentRecord
from .forms import IncidentForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.


class IncidentListView(ListView):
    template_name = "incident_record/incident_list.html"
    paginate_by = 5
    model = IncidentRecord
    context_object_name = "incident_list"

    def get_queryset(self):
        name = self.request.GET.get("short_description")
        if name:
            object_list = self.model.objects.filter(short_description=name)
        else:
            object_list = self.model.objects.all()
        return object_list


class IncidentCreateView(CreateView):
    template_name = "incident_record/incident.html"
    model = IncidentRecord
    form_class = IncidentForm
    context_object_name = "incident"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("incident:incident-list")


class IncidentUpdateView(UpdateView):
    template_name = "incident_record/incident.html"
    form_class = IncidentForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(IncidentRecord, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("incident:incident-list")


class IncidentDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(IncidentRecord, id=id)

    def get_success_url(self):
        return reverse("incident:incident-list")
