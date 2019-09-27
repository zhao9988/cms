from django.db import models
from datetime import datetime
# Create your models here.
class article(models.Model):
    articleId=models.AutoField(primary_key=True)
    headings=models.CharField(max_length=30)
    postdate=models.DateTimeField()
# newarticle=article(headings="新闻1",postdate=datetime.now())
# newarticle.save()
# list=article.objects.values("headings","articleId").get(articleId=2)
# print(list)
# list=article.objects.get(articleId=2)
# print(list.headings)

# article.objects.filter(articleId="3").delete()              #执行有问题

# 更新
# article.objects.filter(articleId="1").update(headings="王五")
# obj = article.objects.get(articleId="2")
# obj.headings = '111'
# obj.save()

# print(article.objects.filter(articleId = "1").count())

# print(article.objects.filter(articleId__gt=1))




