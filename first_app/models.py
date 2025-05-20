from django.db import models
from .constant import DEPARTMENT
# Create your models here.
class Student(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Email=models.EmailField()
    Department=models.CharField(max_length=30,choices=DEPARTMENT)
    Phone_NO=models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.First_name} {self.Last_name}'