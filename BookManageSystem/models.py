from django.db import models

# Create your models here.

class Publisher(models.Model):
    '''
    出版社表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, unique=True)
    addr = models.CharField(max_length=100)


class Book(models.Model):
    '''
    #图书表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, unique=True)
    #和出版社关联的外键
    publisher_id = models.ForeignKey('Publisher', on_delete=models.CASCADE)
