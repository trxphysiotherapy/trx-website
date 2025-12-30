from django.db import models
from django.core.exceptions import ValidationError


class NavBarItem(models.Model):
    """Model to store navigation bar item details."""
    name = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(
        upload_to="navbar_logo/",
        blank=True,
        null=True,
    )

    def clean(self):
        if NavBarItem.objects.exists() and not self.pk:
            raise ValidationError("Only one NavBarItem instance is allowed.")

    def __str__(self):
        return self.name
