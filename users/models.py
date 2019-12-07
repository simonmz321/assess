from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserInfo(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=18)
    phone = models.CharField(max_length=11, default='023-61929176')
    image = models.ImageField(upload_to='media', default='media/user_img/user.jpg')

    def __str__(self):
        return self.name