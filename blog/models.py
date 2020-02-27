from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from django.db import models

class Post(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=60)
    category = models.ManyToManyField('Category',help_text="Select Categories for this Post")
    content = models.TextField()
    banner = models.ImageField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_keyworks = models.CharField("Meta Keywords",max_length=255,
                                     help_text="Comma-delimited set of SEO keywords for meta tag")
    meta_description = models.CharField("Meta Description",max_length=255,
                                     help_text="Content for Description Meta Tag")
    read_time =  models.CharField(max_length=5,null=True,blank=True)

    def get_author(self):
        return self.author.first_name + " " + self.author.last_name

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
