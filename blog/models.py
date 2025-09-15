from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    STATUS_CHOICES= (
        (0, 'Draft'),
        (1, 'Published')
    )
    title = models.CharField(max_length=200)   
    content = models.TextField()  
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    status =  models.IntegerField(choices=STATUS_CHOICES, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    


    def __str__(self):
        return self.title
