from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from django.db.utils import OperationalError

@deconstructible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_owner = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    fullname = models.CharField(max_length=128, default="")
    address = models.CharField(max_length=256, default="")
    rating = models.IntegerField(default=3)

    def __str__(self):
        return self.user.username


class Dog(models.Model):

    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    breed = models.CharField(max_length=128)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="pictures/%Y/%m%d/", max_length=255)
    slug = models.SlugField(unique=True)
    try:
        #owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=UserProfile.objects.first())
        #UserProfile.objects.create(user=User.objects.create_user(username='dummy',email='dummy@example.com', password='password'))
        owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=0)
    except OperationalError:
        pass


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
