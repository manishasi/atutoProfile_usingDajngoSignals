from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name= forms.CharField(max_length=50, required=False)
    last_name= forms.CharField(max_length=50, required=False)
 
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'first_name':None,
            'last_name':None,
            'password1': None,
            'password2': None
            
        }
 
 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']
 
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','father_name','mother_name','dob','city','place']