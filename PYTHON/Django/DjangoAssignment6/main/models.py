from django.db import models
from django.utils import timezone

class Post(models.Model):
    post = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


