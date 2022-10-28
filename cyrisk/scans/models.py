from django.db import models
from hosts.models import Host


class Scan(models.Model):
    host = models.OneToOneField(Host, on_delete=models.CASCADE)
    phase = models.CharField(null=False, max_length=50, default='Scheduled')
    errors = models.TextField(null=True, default=None)
