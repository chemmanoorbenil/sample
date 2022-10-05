from django.db import models

# Create your models here.
class Facebook(models.Model):
    username=models.CharField(max_length=200)
    age=models.IntegerField(default=18)
    father_name=models.CharField(max_length=200)


    def __str__(self):
        return self.username

class Profile(models.Model):
    name=models.CharField(max_length=200)
    profile_img=models.ImageField
    about_me=models.CharField(max_length=200)
    cover_img=models.ImageField


    def __str__(self):
        return self.name




