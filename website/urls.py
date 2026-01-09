from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    about,
    book_appointment,
    blog,
    blog_detail,
    blog_list,
    gallery,
    home,
    services,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("blog/", blog, name="blog"),
    path("services/", services, name="services"),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<str:slug>/', blog_detail, name='blog_detail'),
    path('appointment/', book_appointment, name='appointment'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
