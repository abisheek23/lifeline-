from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class department(models.Model):
    name=models.TextField()


class Staff(models.Model):
    img=models.FileField()
    POSITIONS = [
        ('1', 'Doctor'),
        ('2', 'Pharmacist'),
        ('3', 'Nurse'),
    ]
    name=models.TextField()
    staff_id=models.TextField()
    email=models.EmailField()
    position = models.CharField(max_length=1, choices=POSITIONS)
    department = models.ForeignKey(department, on_delete=models.CASCADE ,null=True,blank=True)
