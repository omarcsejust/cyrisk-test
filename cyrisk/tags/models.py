from django.db import models
import json


class Tag(models.Model):
    name = models.CharField(max_length=250, null=False)
    created = models.DateTimeField(auto_now=True)
    categories = models.TextField(null=True)
    versions = models.TextField(null=True)

    def set_categories(self, cats):
        self.categories = json.dumps(cats)

    def get_categories(self):
        return json.loads(self.categories)

    def set_versions(self, vers):
        self.versions = json.dumps(vers)

    def get_versions(self):
        return json.loads(self.versions)
