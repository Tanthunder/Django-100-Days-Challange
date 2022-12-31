from django.db import models
from django.contrib.auth.models import AbstractUser


#good practice to create your own user model considering future needs.
class CustomUser(AbstractUser):
    """Custom user model."""
    abc = models.CharField(max_length=10, blank=True,null=True)
    
    def __str__(self):
        return self.username


