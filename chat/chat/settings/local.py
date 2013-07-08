from .base import *
import os
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = os.getenv('SECRET_KEY')
