from django.contrib.auth.models import User
from django.db import models
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = f"{random.randint(100000, 999999)}"
        super().save(*args, **kwargs)
