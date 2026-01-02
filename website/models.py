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


class Location(models.Model):
    """Model to store location details."""
    address = models.CharField(max_length=255)
    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True)
    google_map_embed_url = models.TextField(
        help_text="Paste the Google Maps embed URL here"
    )
    
    def clean(self):
        if Location.objects.exists() and not self.pk:
            raise ValidationError("Only one Location instance is allowed.")
    
    def __str__(self):
        return self.address
    

class Testimonial(models.Model):
    """Model to store testimonial details."""
    name = models.CharField(max_length=255)
    content = models.TextField()
    stars = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def clean(self):
        if Testimonial.objects.count() >= 15:
            raise ValidationError("Only 15 testimonial instances are allowed.")

    def __str__(self):
        return self.name
    

class Condition(models.Model):
    """Model to store condition treatment details."""
    title = models.CharField(max_length=200)
    nepali_title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='conditions/')

    def __str__(self):
        return self.title