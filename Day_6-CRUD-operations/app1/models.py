from django.db import models

# Create your models here.
class Student(models.Model):
    """Student model"""
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.name

