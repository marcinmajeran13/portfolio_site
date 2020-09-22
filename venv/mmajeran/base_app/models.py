from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    post_type = (('Repair', 'Repair'), ('Review', 'Review'))

    author = models.CharField(default='Marcin Majeran', max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=32, choices=post_type, default='type')

    def __str__(self):
        return self.title

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

# class Comment(models.Model):
#     pass


class App(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=456, blank=True)
    github_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.name

    def add_app(self):
        self.save()

    def get_absolute_url(self):
        return reverse('app_list')
