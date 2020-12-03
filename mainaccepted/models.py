from django.db import models
from django.utils import timezone

class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    organisation = models.CharField(max_length=50)

    def __str__(self):
        return self.title + '/' + self.organisation

    class Meta:
        verbose_name_plural = "Events"