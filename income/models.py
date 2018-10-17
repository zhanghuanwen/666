from django.db import models

# Create your models here.
class li(models.Model):
    id=models.AutoField(primary_key=True)
    income=models.CharField(max_length=10)