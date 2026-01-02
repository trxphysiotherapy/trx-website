from .models import NavBarItem, Location, Testimonial, Condition
def site_settings(request):
    try:
        return {
            "site_settings": NavBarItem.objects.first(),
            "location": Location.objects.first(),
            "testimonials": Testimonial.objects.all(),
            "conditions": Condition.objects.all()
        }
    except Exception:
        return {
            "site_settings": None,
            "location": None,
            "testimonials": None,
            "conditions": None
        }
