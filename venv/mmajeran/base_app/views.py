from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from base_app.forms import PostForm, ContactForm
from base_app.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.

class Index(generic.TemplateView):
    template_name = 'base_app/index.html'
    
class AboutView(generic.TemplateView):
    template_name = 'base_app/about.html'
    
class ContactView(generic.CreateView):
    template_name = 'base_app/contact.html'
    form_class = ContactForm

    
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

# def sendEmail(request):
#     if request.method == 'POST':
#
#         template = 'base_app/contact.html', {
#             'name':request.POST['name'],
#             'email':request.POST['email'],
#             'messsage':request.POST['message'],
#         }
#
#         email = EmailMessage(
#             request.POST['subject'],
#             template,
#             settings.EMAIL_HOST_USER,
#             ['m4cin878@gmail.com']
#         )
#
#         email.fail_silently=False
#         email.send()
#
#     return render(request, 'base_app/email_sent.html')
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['email']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['marcin.majeran.contact@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "base_app/contact.html", {'form': form})

def successView(request):
    return render(request, 'base_app/email_sent.html')