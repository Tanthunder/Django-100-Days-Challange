from django.db import models

from app1.models import CustomUser

import random
# Create your models here.

class Code(models.Model):
    """Code model."""
    number = models.CharField(max_length=5,blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self,*args,**kwargs):
        """Generating random code when save method gets executed on CustomUser model. Post_save signal is used."""
        num_list = [i for i in range(10)]
        code_list = []
        for i in range(5):
            num = random.choice(num_list)
            code_list.append(num)
        print(code_list)
        code_str = "".join(str(i) for i in code_list)
        self.number = code_str
        super().save(*args,**kwargs)