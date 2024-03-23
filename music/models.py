from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustUser(AbstractUser):
    new=models.CharField(max_length=100)

class Music(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='music')
    img=models.ImageField(upload_to='thumbnail')
    choices=(
        ('Angry','Angry'),
        ('Disgust','Disgust'),
        ('Fear','Fear'),
        ('Happy','Happy'),
        ('Neutral','Neutral'),
        ('Sad','Sad'),
        ('Surprise','Surprise'),
    )
    type=models.CharField(max_length=100,choices=choices)



class Score(models.Model):
    score = models.IntegerField()
    mood = models.CharField(max_length=50)


class Emotion(models.Model):
    emotion=models.CharField(max_length=100)  
    timestamp = models.DateTimeField(auto_now_add=True,null=True)  