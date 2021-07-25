from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to = "uploads/blog-picture/")
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    cardDescription = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title