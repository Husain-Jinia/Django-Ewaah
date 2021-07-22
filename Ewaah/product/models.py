from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'uploads/photos/', null=True, blank=True)

    def __str__(self):
        return self.title