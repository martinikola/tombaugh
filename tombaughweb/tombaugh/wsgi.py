"""
WSGI config for tombaugh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib          # new

import dotenv           # new

from django.core.wsgi import get_wsgi_application

# BASE_DIR = Path(__file__).resolve().parent.parent     # new
CURRENT_DIR = pathlib.Path(__file__).resolve().parent   # new
BASE_DIR = CURRENT_DIR.parent                           # new
ENV_FILE_PATH = BASE_DIR / ".env"                       # new

dotenv.load_dotenv(str(ENV_FILE_PATH))                 # new
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tombaugh.settings')

application = get_wsgi_application()
