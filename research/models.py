from django.db import models
from django.contrib.auth.models import User

class ResearchSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    status = models.CharField(max_length=20, default="PENDING")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    trace_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ResearchSummary(models.Model):
    research = models.OneToOneField(ResearchSession, on_delete=models.CASCADE)
    summary = models.TextField(blank=True)

class ResearchReasoning(models.Model):
    research = models.OneToOneField(ResearchSession, on_delete=models.CASCADE)
    reasoning = models.TextField(blank=True)

class ResearchCost(models.Model):
    research = models.OneToOneField(ResearchSession, on_delete=models.CASCADE)
    input_tokens = models.IntegerField(default=0)
    output_tokens = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0)

class UploadedDocument(models.Model):
    research = models.ForeignKey(
        ResearchSession,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    file = models.FileField(upload_to="uploads/")
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
