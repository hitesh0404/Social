from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    like = models.ManyToManyField(Person)
class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='media/post/image',default='')

