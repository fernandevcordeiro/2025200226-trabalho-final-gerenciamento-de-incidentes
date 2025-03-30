from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class IncidentRecord(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("on_hold", "On Hold"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
        ("canceled", "Canceled"),
    ]

    IMPACT_CHOICES = [(1, "High"), (2, "Medium"), (3, "Low")]
    URGENCY_CHOICES = [(1, "High"), (2, "Medium"), (3, "Low")]
    PRIORITY_CHOICES = [(1, "High"), (2, "Medium"), (3, "Low")]

    CHANNEL_CHOICES = [
        ("event", "Event"),
        ("email", "Email"),
        ("phone", "Phone"),
        ("self_service", "Self-service"),
        ("chat", "Chat"),
    ]

    CATEGORY_CHOICES = [
        ("access_account", "Access/Account"),
        ("client_application", "Client Application"),
        ("data", "Data"),
        ("event_management", "Event Management"),
        ("hardware", "Hardware"),
        ("inquiry_help", "Inquiry/Help"),
        ("licenses_certificates", "Licenses & Certificates"),
        ("network", "Network"),
        ("security", "Security"),
        ("software", "Software"),
    ]

    ENVIRONMENT_CHOICES = [
        ("production", "Production"),
        ("qa", "QA"),
        ("staging", "Staging"),
        ("development", "Development"),
        ("sandbox", "Sandbox"),
        ("testing", "Testing"),
        ("uat", "UAT"),
    ]

    ASSIGNMENT_GROUP_CHOICES = [
        ("support_team", "Support Team"),
        ("development_team", "Development Team"),
        ("devops_team", "DevOps Team"),
    ]

    ON_HOLD_REASONS = [
        ("awaiting_info", "Awaiting Additional Information"),
        ("third_party_dependency", "Dependency on Third Parties/Other Teams"),
        ("maintenance_window", "Maintenance Window Needed"),
        ("awaiting_approval", "Awaiting Approval"),
        ("issue_stopped", "Issue Has Stopped Occurring"),
    ]

    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidents")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_incidents",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_incidents",
    )
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deleted_incidents",
    )
    active = models.BooleanField(default=True)
    impact = models.IntegerField(choices=IMPACT_CHOICES)
    urgency = models.IntegerField(choices=URGENCY_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    impacted_item = models.CharField(max_length=255, null=True, blank=True)
    owner_item = models.CharField(max_length=255, null=True, blank=True)
    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    assignment_group = models.CharField(
        max_length=30, choices=ASSIGNMENT_GROUP_CHOICES, null=True, blank=True
    )
    assignment_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_incidents",
    )
    on_hold_reasons = models.CharField(
        max_length=50, choices=ON_HOLD_REASONS, null=True, blank=True
    )
    duration = models.DurationField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    activity = models.TextField(null=True, blank=True)
    parent_incident = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="child_incidents",
    )
    child_incident = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parent_incidents",
    )
    resolved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="resolved_incidents",
    )
    resolved_date = models.DateTimeField(null=True, blank=True)
    closed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="closed_incidents",
    )
    closed_date = models.DateTimeField(null=True, blank=True)
    closure_notes = models.TextField(null=True, blank=True)
    root_cause = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.short_description} ({self.status})"

    def get_absolute_url(self):
        return reverse("incident:incident-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("incident:incident-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "incident_record"
