from django.urls import path
from . import views


urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    # path('contact/',views.ContactView.as_view(),name='contact'),
    path('post_list/',views.WritingView.as_view(),name='post_list'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<slug/publish/', views.post_publish, name='post_publish'),
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
    path('app_list/',views.AppsView.as_view(),name='app_list'),
    path('app/new/', views.CreateAppView.as_view(), name='app_new'),
    path('app/<slug>/edit/', views.AppUpdateView.as_view(), name='app_edit'),
    path('app/<slug>/remove/', views.AppDeleteView.as_view(), name='app_remove'),
    path('app/<slug>/publish/', views.app_add, name='app_add'),
]