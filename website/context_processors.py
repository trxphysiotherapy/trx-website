from django.core.paginator import Paginator

from .models import BlogPost, Condition, Location, NavBarItem, Service, Testimonial


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
    
        return {
            "site_settings": NavBarItem.objects.first(),
            "location": Location.objects.first(),
            "testimonials": Testimonial.objects.all(),
            "conditions": Condition.objects.all(),
            "left_services": all_services[:middle],
            "right_services": all_services[middle:],
            "all_blog_posts": page_obj,
        }
    except Exception:
        return {
            "site_settings": None,
            "location": None,
            "testimonials": None,
            "left_services": None,
            "right_services": None,
            "all_blog_posts": None,
        }
