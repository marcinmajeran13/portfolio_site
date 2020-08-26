from django.urls import path
from . import views


urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('writing/',views.WritingView.as_view(),name='writing'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<slugk>/publish/', views.post_publish, name='post_publish'),

]