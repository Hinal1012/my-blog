from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField
from django.db.models.signals import pre_save
from .util import unique_slug_generator

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_num = models.BigIntegerField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', default='default/default.png')

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null = True, blank = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(null=True, blank=True)
    video_url = EmbedVideoField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

def post_pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

pre_save.connect(post_pre_save_receiver, sender = Post) 


class Aboutus(models.Model):
    updated_on = models.DateTimeField(auto_now= True)
    profile_pic = models.ImageField(upload_to='about/', default='default/default.png')
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name