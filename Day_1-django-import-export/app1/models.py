from django.db import models


# Day 1
class Student(models.Model):
    """Model for student details."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_studying = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """For string representation."""
        return str(self.name)