from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
