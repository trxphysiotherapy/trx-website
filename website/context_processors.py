from .models import NavBarItem, Location

def site_settings(request):
    try:
        return {
            "site_settings": NavBarItem.objects.first(),
            "location": Location.objects.first()
        }
    except Exception:
        return {
            "site_settings": None,
            "location": None
        }
