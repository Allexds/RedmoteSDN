"""
WSGI config for RedmoteWEB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys


sys.path.append('/var/www/html/RedmoteSDN/RedmoteWEB/RedmoteWEB/')

sys.path.append('/var/www/html/RedmoteSDN/RedmoteWEB/linux-venv/lib/python3.6/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedmoteWEB.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
