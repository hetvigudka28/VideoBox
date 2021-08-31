from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
#from django.contrib.validators import FileExtensionValidator

# Create your models here.
class Videos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title=models.CharField(max_length=250, default="")
    description=models.TextField(max_length=1000, default="")
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    date=models.CharField(default="", max_length=100)
    thumbnail=models.ImageField(upload_to='thumbnail_uploaded',null=True, blank=True)
    video=models.FileField(upload_to="videos_uploaded", validators=[FileExtensionValidator(['MOV','avi','mp4','webm','mkv'])], default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    video = models.ForeignKey(Videos,on_delete=models.CASCADE,default="")
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text
