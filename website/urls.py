from django.urls import path
from .views import home, about, gallery, blog, services, blog_list, blog_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("blog/", blog, name="blog"),
    path("services/", services, name="services"),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<str:slug>/', blog_detail, name='blog_detail'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
