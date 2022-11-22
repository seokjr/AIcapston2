from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.text
        
class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title

class Grouprecommend(models.Model):
    group_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)