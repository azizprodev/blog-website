from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
