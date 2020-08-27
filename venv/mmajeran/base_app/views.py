from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from base_app.forms import PostForm
from base_app.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

class Index(generic.TemplateView):
    template_name = 'base_app/index.html'
    
class AboutView(generic.TemplateView):
    template_name = 'base_app/about.html'
    
class ContactView(generic.TemplateView):
    template_name = 'base_app/contact.html'
    
class WritingView(generic.ListView):
    model = Post
    # 
    # def get_queryset(self):
    #     return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    
class PostDetailView(generic.DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    
    
@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug)