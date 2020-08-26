from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.publish_date = timezone.now()
        self.slug = slugify(self.title)
        self.save()
    
    def get_abosulte_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})
        
     
# class Comment (models.Model):
#     pass
