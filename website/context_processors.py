from .models import NavBarItem

def site_settings(request):
    settings = NavBarItem.objects.first()
    return {
        'site_settings': settings
    }
