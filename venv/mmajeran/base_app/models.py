from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.CharField(default='Marcin Majeran',max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def publish(self):
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
        
     
# class Comment (models.Model):
#     pass
