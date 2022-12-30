from django.db import models


# Create your models here.
class App1Model(models.Model):
    name= models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name
