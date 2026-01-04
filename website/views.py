from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def blog(request):
    return render(request, 'main/blog.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def blog_list(request):
    post_list = BlogPost.objects.all().order_by('-created_at')
    
    # Show 6 posts per page
    paginator = Paginator(post_list, 6) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # We pass 'page_obj' to the template
    return render(request, 'main/blog.html', {'all_blog_posts': page_obj})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'main/blog_detail.html', {'post': post})