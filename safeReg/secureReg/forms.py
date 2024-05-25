from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

class UserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    captcha = ReCaptchaField()