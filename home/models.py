from django.db import models
from django.conf import settings

class Status(models.Model):
    user = models.IntegerField()  # Assuming user is represented by an integer ID; replace with ForeignKey if referencing User model
    status = models.IntegerField()  # Field for status (0, 1, 2, etc.)

    def __str__(self):
        return f"Status for User {self.user}: {self.status}"

