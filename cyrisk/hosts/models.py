from django.db import models


class Host(models.Model):
    name = models.CharField(null=False, max_length=50)
    domain = models.CharField(max_length=255, null=False)
    description = models.TextField()
    criticality = models.CharField(null=False, max_length=50)



