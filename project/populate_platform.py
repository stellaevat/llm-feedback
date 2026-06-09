import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()
from app.models import Assignment

def populate():
    pass

def add_assignment():
    pass

if __name__ == '__main__':
    print("Starting platform population script...")
    populate()