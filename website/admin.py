from django.contrib import admin
from django.utils.html import format_html

from .models import (
    BlogPost,
    Condition,
    GalleryImage,
    Location,
    NavBarItem,
    Service,
    Testimonial,
    VideoContent,
)

admin.site.register(NavBarItem)
admin.site.register(Location)
admin.site.register(Testimonial)
admin.site.register(Condition)
admin.site.register(Service)
admin.site.register(BlogPost)
admin.site.register(VideoContent)
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'created_at')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"