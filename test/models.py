from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# #정답DB (정답id, 유저아이디, 문제아이디, 유저의 답, 정답여부)
# class LevelTests(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
#     # test_id = models.ForeignKey("TestImages", related_name="test", on_delete=models.CASCADE, db_column="test_id")
#     answer = models.IntegerField(null=False)
#     correct = models.BooleanField()
#     title = models.TextField()
    
#레벨테스트DB (문제아이디, 이미지, 답, 분류)
class TestImages(models.Model): 
    test_id = models.BigAutoField(help_text="test_id",primary_key=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) 
    answer = models.IntegerField()
    title_id = models.ForeignKey('title', on_delete=models.CASCADE, db_column='title_id')
    
    
# class answer(models.Model):
#     answer = models.IntegerField(null=True)
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    
class total(models.Model):
    test_id = models.ForeignKey('TestImages', on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    category = models.IntegerField(null=True)
    correct = models.IntegerField()
    
    
    
    
class title(models.Model):
    title_id = models.IntegerField(help_text="title_id",primary_key=True)
    big_title = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=20, null=True)
    
class grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title_id = models.ForeignKey('title', on_delete=models.CASCADE, db_column='title_id')
    total = models.IntegerField(null=True)




    
    

    
    
  
    
