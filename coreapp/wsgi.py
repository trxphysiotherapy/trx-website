import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root to sys.path so Django can find the 'coreapp' module
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreapp.settings')

application = get_wsgi_application()
app = application