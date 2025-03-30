from django.contrib import admin
from .models import IncidentRecord


# Register your models here.
@admin.register(IncidentRecord)
class IncidentRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "short_description", "impact"]
