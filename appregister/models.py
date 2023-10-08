from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', blank=True, null=True)