from django.db import models
from django.db.models.enums import Choices

# Create your models here.
gender_choice=[('male','MALE'),('female',"FEMALE")]

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fees = models.IntegerField()

    def __str__(self):
        return self.first_name