from django.db import models
#module 数据库ORM   py-->ORM ---> 数据库驱动-->sqlite3
#ORM把写SQL语句屏蔽了 可操作类方法一样操作数据库
#首先安装orm方式创建表
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #null=True 默认可以为空
    question_desc = models.TextField(null=True,default='')
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)