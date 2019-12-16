'''Modules'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''Create user form'''
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'date_of_birth')

class CustomUserChangeForm(UserChangeForm):
    '''Alter user form'''
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'date_of_birth')
