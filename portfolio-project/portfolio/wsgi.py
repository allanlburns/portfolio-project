import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

# import os

# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# application = Cling(get_wsgi_application())
