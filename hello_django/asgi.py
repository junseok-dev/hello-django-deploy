"""
ASGI config for hello_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
# blacknoise: production(asgi) 환경에서 django 자체적으로 static 서빙을 지원하는 패키지
from blacknoise import BlackNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings.development')

application = BlackNoise(get_asgi_application())
application.add(settings.BASE_DIR / 'static', '/static')
