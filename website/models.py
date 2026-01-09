import re

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


class VideoContent(models.Model):
    """Model to store video content details for TikTok and YouTube videos."""

    PLATFORM_CHOICES = [
        ("tiktok", "TikTok"),
        ("youtube", "YouTube"),
    ]

    title = models.CharField(max_length=200, null=True)
    embedded_url = models.TextField(
        help_text="Paste the YouTube link, TikTok link, or full Embed code here"
    )
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    processed_id = models.CharField(max_length=255, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        if not self.pk and VideoContent.objects.count() >= 20:
            raise ValidationError("You can only have a maximum of 20 videos.")

    def save(self, *args, **kwargs):
        if self.platform == "youtube":
            yt_match = re.search(
                r"(?:v=|\/v\/|embed\/|shorts\/|youtu.be\/)([a-zA-Z0-9_-]{11})",
                self.embedded_url,
            )
            if yt_match:
                self.processed_id = yt_match.group(1)

        elif self.platform == "tiktok":
            tt_match = re.search(r"video/(\d+)", self.embedded_url)
            if tt_match:
                self.processed_id = tt_match.group(1)
            else:
                tt_id_match = re.search(r'data-video-id="(\d+)"', self.embedded_url)
                if tt_id_match:
                    self.processed_id = tt_id_match.group(1)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.platform.capitalize()} - {self.title}"


class GalleryImage(models.Model):
    """Model to store gallery image details."""

    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")
    alt_text = models.CharField(max_length=200, default="Gallery Image")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.pk and GalleryImage.objects.count() >= 20:
            raise ValidationError("You can only have a maximum of 20 gallery images.")

    def __clstr__(self):
        return self.title or f"Image {self.id}"


class TeamMember(models.Model):
    """Model to store team member details."""

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name


class Company(models.Model):
    """Model to store company details."""

    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)

    def clean(self):
        if Company.objects.exists() and not self.pk:
            raise ValidationError("Only one Company instance is allowed.")

    def __str__(self):
        return self.full_name


class SEOTitleAndMetaDescription(models.Model):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("about", "About"),
        ("service", "Services"),
        ("gallery", "Gallery"),
        ("blog", "Blog"),
    ]

    page_type = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        unique=True,
        help_text="Select the page this SEO data belongs to.",
    )
    title = models.CharField(
        max_length=100, help_text="Include Title from 50 to 65 characters."
    )
    meta_description = models.TextField(
        help_text="Include Meta Description from 70 to 150 characters."
    )

    class Meta:
        verbose_name = "SEO Setting"
        verbose_name_plural = "SEO Settings"

    def clean(self):
        exists = (
            SEOTitleAndMetaDescription.objects.filter(page_type=self.page_type)
            .exclude(pk=self.pk)
            .exists()
        )
        if exists:
            raise ValidationError(
                f"SEO settings for the '{self.get_page_type_display()}' page already exist."
            )

    def __str__(self):
        return f"{self.get_page_type_display()} - {self.title}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Followed Up / Completed"),
        ("cancelled", "Cancelled"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=False)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"


# Proxy models for separate Admin views
class NewRequest(Appointment):
    class Meta:
        proxy = True
        verbose_name = "New Request"
        verbose_name_plural = "New Requests"


class CompletedRecord(Appointment):
    class Meta:
        proxy = True
        verbose_name = "Followed-up Record"
        verbose_name_plural = "Followed-up Records"
