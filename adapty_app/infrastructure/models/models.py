from django.db import models

from adapty_app.domains.entities.enums import Gender, Platform


class User(models.Model):
    profile_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(
        max_length=16,
        choices=Gender.choices(),
        null=True,
        blank=True
    )
    email = models.EmailField(null=True, blank=True)


class Device(models.Model):
    device_id = models.UUIDField(primary_key=True)
    app_version = models.CharField(max_length=16)
    platform = models.CharField(max_length=16, choices=Platform.choices())
    timezone = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
