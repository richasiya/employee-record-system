from django.db import models
class Student(models.Model):
    name =models.CharField(max_length = 200)
    college =models.CharField(max_length = 200)
    is_active =models.BooleanField(default=False)
    age =models.IntegerField(max_length = 10)
# Create your models here.
