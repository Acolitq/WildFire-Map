from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class FireReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.username if self.user else 'Anonymous'} at ({self.latitude}, {self.longitude})"