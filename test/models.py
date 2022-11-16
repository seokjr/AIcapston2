from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#정답DB (정답id, 유저아이디, 문제아이디, 유저의 답, 정답여부)
class LevelTests(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    test_id = models.ForeignKey("TestImages", related_name="test", on_delete=models.CASCADE, db_column="test_id")
    answer = models.IntegerField()
    correct = models.BooleanField()
    title = models.TextField()
    
#레벨테스트DB (문제아이디, 이미지, 답, 분류)
class TestImage(models.Model): 
    test_id = models.BigAutoField(help_text="test_id",primary_key=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) 
    answer = models.IntegerField()
    bigtitle = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=20, null=False)
  
    
