from .models import NavBarItem

def site_settings(request):
    try:
        return {
            "site_settings": NavBarItem.objects.first()
        }
    except Exception:
        return {
            "site_settings": None
        }
