from django.db import models
from django.utils import timezone

class CowText(models.Model):
    text = models.CharField(max_length=250)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text