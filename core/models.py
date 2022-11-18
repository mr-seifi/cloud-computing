from django.db import models
from advertising.storage_backends import MediaStorage
from .enums import AdCategory


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(storage=MediaStorage())
    category = models.CharField(max_length=255, choices=AdCategory.choices, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
