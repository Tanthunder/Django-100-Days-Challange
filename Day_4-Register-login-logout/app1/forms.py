from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser
from django.forms import ModelForm



class CustomUserCreationForm(UserCreationForm):
    class Meta :
        model = CustomUser
        fields = ['first_name','email','username','password1','password2','abc']


        