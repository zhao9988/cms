from django.db import models
# Create your models here.
class user(models.Model):
    userId=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.IntegerField()
    email = models.CharField(max_length=50)
    time = models.DateTimeField()





