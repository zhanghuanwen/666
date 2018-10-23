# from django.db import models
# import json
# from sex.models import li as sex_li
# from income.models import li as income_li
# from education.models import li as edu_li
#
# # Create your models here.
#
# class regist(models.Model):
#     id=models.AutoField(primary_key=True)
#     tel=models.CharField(max_length=11,null=False)
#     password=models.CharField(max_length=100,null=False)
#     sex=models.ForeignKey(to=sex_li,to_field='id',on_delete=True)
#     pub_time=models.DateTimeField(auto_now_add=True)
# #
# class base(models.Model):
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=50)
#     sex = models.ForeignKey(to=sex_li,to_field='id',on_delete=True)
#     birth=models.DateField(null=True)
#     height=models.CharField(max_length=5,null=True)
#     income=models.ForeignKey(to=income_li,to_field='id',null=True,on_delete=models.SET_NULL)
#     marry=models.CharField(max_length=20,null=True)
#     edu=models.ForeignKey(to=edu_li,to_field='id',null=True,on_delete=models.SET_NULL)
#     city=models.CharField(max_length=20,null=True)
#     signature=models.CharField(max_length=400,null=True)
#     img_src=models.CharField(max_length=50,null=True)
#
# class hobby(models.Model):
#     id=models.AutoField(primary_key=True)
#     food=models.CharField(max_length=100,null=True)
#     music=models.CharField(max_length=100,null=True)
#     film=models.CharField(max_length=100,null=True)
#     book=models.CharField(max_length=100,null=True)
#     pet=models.CharField(max_length=100,null=True)
#
# class life(models.Model):
#     id=models.AutoField(primary_key=True)
#     drink=models.CharField(max_length=50,null=True)
#     smoke=models.CharField(max_length=50,null=True)
#     car=models.CharField(max_length=50,null=True)
#     cook=models.CharField(max_length=50,null=True)
#     housework=models.CharField(max_length=50,null=True)
#     parent=models.CharField(max_length=50,null=True)
#
# class message(models.Model):
#     id=models.AutoField(primary_key=True)
#     addr=models.CharField(max_length=50,null=True)
#     weight=models.CharField(max_length=5,null=True)
#     constellation=models.CharField(max_length=20,null=True)
#     blood=models.CharField(max_length=10,null=True)
#     nation=models.CharField(max_length=10,null=True)
#     profession=models.CharField(max_length=20,null=True)
#     house=models.CharField(max_length=20,null=True)
#     school=models.CharField(max_length=20,null=True)
#     children=models.CharField(max_length=20,null=True)