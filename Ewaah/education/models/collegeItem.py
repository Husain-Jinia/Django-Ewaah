from django.db import models
from .college import College
from django.contrib.auth.models import User

class CollegeItem(models.Model):
    name = models.CharField(max_length=100, )
    description = models.CharField(max_length=100, default='')
    warranty = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to = 'uploads/photos/')
    image2 = models.ImageField(upload_to = 'uploads/photos/')
    image3 = models.ImageField(upload_to = 'uploads/photos/')
    donator = models.ForeignKey(User,on_delete=models.CASCADE)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.college}'
    

    