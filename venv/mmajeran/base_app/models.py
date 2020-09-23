from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Post(models.Model):
    post_type = (('Repair', 'Repair'), ('Review', 'Review'))

    author = models.CharField(default='Marcin Majeran', max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=32, choices=post_type, default='type')
    slug = models.SlugField(unique=True, default=publish_date)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

# class Comment(models.Model):
#     pass


class App(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=456, blank=True)
    github_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    # image = models.ImageField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(App, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('app_list')
