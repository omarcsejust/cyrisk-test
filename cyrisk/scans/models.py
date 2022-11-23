from django.db import models
from hosts.models import Host
from tags.models import Tag


class Scan(models.Model):

    PHASE_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Running", "Running"),
        ("Complete", "Complete"),
        ("Error", "Error")
    ]

    host = models.OneToOneField(Host, on_delete=models.CASCADE)
    phase = models.CharField(null=False, max_length=50, default='Scheduled', choices=PHASE_CHOICES)
    errors = models.TextField(null=True, default=None)
    tags = models.ManyToManyField(Tag)
