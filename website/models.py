from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    image = models.ImageField(upload_to="conditions/")

    def __str__(self):
        return self.title


class Service(models.Model):
    """Model to store service details."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    points = models.TextField(help_text="Enter each point on a new line")

    def __str__(self):
        return self.title

    def get_points_list(self):
        return self.points.splitlines()


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    tag = models.CharField(max_length=50)  # e.g., "Technology"
    tag_class = models.CharField(max_length=20, default="tag-teal")  # for CSS colors
    content = RichTextUploadingField()
    image = models.ImageField(
        upload_to="blog_img/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
