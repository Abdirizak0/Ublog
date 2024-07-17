from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    template_path = os.path.join(settings.BASE_DIR, 'Ablog', 'templates', 'Ablog', 'index.html')
    return render(request, template_path)