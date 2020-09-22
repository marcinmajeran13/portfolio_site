from django.urls import path
from . import views


urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    # path('contact/',views.ContactView.as_view(),name='contact'),
    path('post_list/',views.WritingView.as_view(),name='post_list'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
    path('app_list/',views.AppsView.as_view(),name='app_list'),
    path('app/new/', views.CreateAppView.as_view(), name='app_new'),
    path('app/<int:pk>/edit/', views.AppUpdateView.as_view(), name='app_edit'),
    path('app/<int:pk>/remove/', views.AppDeleteView.as_view(), name='app_remove'),
    path('app/<int:pk>/publish/', views.app_add, name='app_add'),
]