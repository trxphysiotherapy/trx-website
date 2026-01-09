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
    TeamMember,
    Company,
    SEOTitleAndMetaDescription,
    NewRequest,
    CompletedRecord,
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

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
admin.site.register(Company)
admin.site.register(SEOTitleAndMetaDescription)

class BaseAppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date', 'status')
    list_filter = ('service', 'date')
    search_fields = ('name', 'phone')
    list_editable = ('status',)


@admin.register(NewRequest)
class NewRequestAdmin(admin.ModelAdmin):
    # Change 'service' to 'phone' or 'email' and 'date' to 'created_at'
    list_display = ('name', 'phone', 'created_at', 'status') 
    list_filter = ('created_at',) # Removed 'service' as it doesn't exist
    
    def get_queryset(self, request):
        # Only show 'pending' requests in this view
        return super().get_queryset(request).filter(status='pending')

@admin.register(CompletedRecord)
class CompletedRecordAdmin(admin.ModelAdmin):
    # Match the fields here as well
    list_display = ('name', 'phone', 'created_at', 'status')
    list_filter = ('created_at',)
    
    def get_queryset(self, request):
        # Only show 'completed' records in this view
        return super().get_queryset(request).filter(status='completed')