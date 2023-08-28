from django.views.generic.edit import CreateView
from .models import Organization


class Add(CreateView):
    model = Organization
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/organization/'