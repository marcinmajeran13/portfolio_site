from django.shortcuts import render
from django.views import generic

# Create your views here.

class Index(generic.TemplateView):
    template_name = 'base_app/index.html'
    
class AboutView(generic.TemplateView):
    template_name = 'base_app/about.html'
    
class ContactView(generic.TemplateView):
    template_name = 'base_app/contact.html'
