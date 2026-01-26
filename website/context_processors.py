from django.core.paginator import Paginator

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
    SlideshowImage,
    CoreService,
)


def site_settings(request):
    try:
        # Services
        all_services = Service.objects.all()
        count = all_services.count()
        middle = (count + 1) // 2

        # Blog
        blog_queryset = BlogPost.objects.all().order_by('-created_at')
        paginator = Paginator(blog_queryset, 8)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Gallery
        videos = VideoContent.objects.all()
        tiktok_videos = videos.filter(platform='tiktok')
        youtube_videos = videos.filter(platform='youtube')

        # Image
        images = GalleryImage.objects.all().order_by('-created_at')

        # SEO Title and Meta Description
        home = SEOTitleAndMetaDescription.objects.filter(page_type='home').first()
        about = SEOTitleAndMetaDescription.objects.filter(page_type='about').first()
        service = SEOTitleAndMetaDescription.objects.filter(page_type='service').first()
        blog = SEOTitleAndMetaDescription.objects.filter(page_type='blog').first()
        gallery = SEOTitleAndMetaDescription.objects.filter(page_type='gallery').first()

        # Slider Image
        slideshow_images = SlideshowImage.objects.all()

        return {
            "site_settings": NavBarItem.objects.first(),
            "location": Location.objects.first(),
            "testimonials": Testimonial.objects.all(),
            "conditions": Condition.objects.all(),
            "left_services": all_services[:middle],
            "right_services": all_services[middle:],
            "all_blog_posts": page_obj,
            "tiktok_videos": tiktok_videos,
            "youtube_videos": youtube_videos,
            "images": images,
            "team": TeamMember.objects.all(),
            "company": Company.objects.first(),
            "home": home,
            "about": about,
            "service": service,
            "blog": blog,
            "gallery": gallery,
            "slideshow_images": slideshow_images,
            "core_services": CoreService.objects.all(),

        }
    except Exception:
        return {
            "site_settings": None,
            "location": None,
            "testimonials": None,
            "left_services": None,
            "right_services": None,
            "all_blog_posts": None,
            "tiktok_videos": None,
            "youtube_videos": None,
            "images": None,
            "team": None,
            "company": None,
            "home": None,
            "about": None,
            "service": None,
            "blog": None,
            "gallery": None,
            "slideshow_images": None
            
        }
