from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'photo', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
