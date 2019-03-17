from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Dog(models.Model):

    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    breed = models.CharField(max_length=128)
    image = models.ImageField(upload_to="pictures/%Y/%m%d/", max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username    
