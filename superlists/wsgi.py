"""
WSGI config for superlists project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/testing-goat')

load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")

application = get_wsgi_application()
