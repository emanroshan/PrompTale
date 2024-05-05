from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username','profile_picture', 'password1', 'password2', )

class AccountAuthenticationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
            
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'password')
    
class UpdateForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    image = forms.ImageField()
