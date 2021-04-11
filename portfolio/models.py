from django.db import models
from django.urls import reverse

import uuid

class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    cover = models.ImageField(upload_to='covers/')
    url_github = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
