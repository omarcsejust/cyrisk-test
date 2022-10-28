from django.db import models
from django.core.validators import URLValidator


class Host(models.Model):
    name = models.CharField(null=False, max_length=50)
    # TODO:: here we can implement a custom validators to validate domain, I have a plan to do it later
    domain = models.CharField(max_length=255, null=False, validators=[URLValidator])
    description = models.TextField()
    criticality = models.CharField(null=False, max_length=50)


