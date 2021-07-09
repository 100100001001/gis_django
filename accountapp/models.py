from django.db import models

# Create your models here.


class NewModel(models.Model): # 장고에서 제공해주는 기초 모델!
    text = models.CharField(max_length=255, null=False)
