import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'blogicum'))
sys.path.insert(0, os.path.join(current_dir, 'blogicum', 'blogicum'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()
