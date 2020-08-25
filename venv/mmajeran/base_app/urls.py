from django.urls import path
from . import views


urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('writing/',views.WritingView.as_view(),name='writing'),
]