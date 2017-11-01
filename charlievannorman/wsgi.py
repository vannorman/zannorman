"""
WSGI config for charlievannorman project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import sys
sys.path.append('/home/ubuntu/charlievannorman.com')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "charlievannorman.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
