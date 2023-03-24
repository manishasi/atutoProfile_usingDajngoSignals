from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Create your models here.

 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    father_name = models.CharField(max_length=50,default=None,null=True,blank=True)
    mother_name = models.CharField(max_length=50,default=None,null=True,blank=True)
    dob = models.DateField(max_length=8,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    place = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'