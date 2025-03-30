from django import forms
from .models import IncidentRecord
from django.contrib.auth.models import User


class IncidentForm(forms.ModelForm):
    caller = forms.ModelChoiceField(
        label="Reportado por:", queryset=User.objects.all(), required=True
    )
    status = forms.ChoiceField(
        label="Status", choices=IncidentRecord.STATUS_CHOICES, required=True
    )
    description = forms.CharField(
        label="Descrição", widget=forms.Textarea, required=True
    )
    short_description = forms.CharField(
        label="Descrição curta", max_length=255, required=True
    )
    impact = forms.ChoiceField(
        label="Impacto", choices=IncidentRecord.IMPACT_CHOICES, required=True
    )
    urgency = forms.ChoiceField(
        label="Urgencia", choices=IncidentRecord.URGENCY_CHOICES, required=True
    )
    priority = forms.ChoiceField(
        label="Prioridade", choices=IncidentRecord.PRIORITY_CHOICES, required=True
    )
    channel = forms.ChoiceField(
        label="Canal", choices=IncidentRecord.CHANNEL_CHOICES, required=True
    )
    category = forms.ChoiceField(
        label="Categoria", choices=IncidentRecord.CATEGORY_CHOICES, required=True
    )
    impacted_item = forms.CharField(
        label="Item Impactado:", max_length=255, required=False
    )
    owner_item = forms.CharField(
        label="Responsável pelo Item:", max_length=255, required=False
    )
    environment = forms.ChoiceField(
        label="Ambiente", choices=IncidentRecord.ENVIRONMENT_CHOICES, required=True
    )
    assignment_group = forms.ChoiceField(
        label="Assinado para o Grupo:",
        choices=IncidentRecord.ASSIGNMENT_GROUP_CHOICES,
        required=False,
    )
    assignment_to = forms.ModelChoiceField(
        label="Assinado para", queryset=User.objects.all(), required=False
    )
    on_hold_reasons = forms.ChoiceField(
        label="Motivo do Status 'On hold'",
        choices=IncidentRecord.ON_HOLD_REASONS,
        required=False,
    )
    notes = forms.CharField(label="Notas", widget=forms.Textarea, required=False)
    parent_incident = forms.ModelChoiceField(
        label="Incidente Pai", queryset=IncidentRecord.objects.all(), required=False
    )
    child_incident = forms.ModelChoiceField(
        label="Incidente Filho", queryset=IncidentRecord.objects.all(), required=False
    )

    class Meta:
        model = IncidentRecord
        fields = (
            "caller",
            "status",
            "description",
            "short_description",
            "impact",
            "urgency",
            "priority",
            "channel",
            "category",
            "impacted_item",
            "owner_item",
            "environment",
            "assignment_group",
            "assignment_to",
            "on_hold_reasons",
            "notes",
            "parent_incident",
            "child_incident",
        )
