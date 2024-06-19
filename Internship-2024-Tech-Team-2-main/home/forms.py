from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import UserProfile

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already taken")
        return email



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Password'}))




class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'mobile_number', 'information', 'email']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    subject = forms.CharField(max_length=200, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
