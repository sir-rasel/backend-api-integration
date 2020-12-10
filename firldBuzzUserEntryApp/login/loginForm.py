from django import forms

class LoginForm(forms.Form):
    userName = forms.EmailField(label='User Name', max_length=55, required=True, \
        widget=forms.EmailInput(attrs={'placeholder': 'Username that sends via mail'}))
    password = forms.CharField(label='Password', max_length=55, required=True, \
        widget=forms.PasswordInput(attrs={'placeholder': 'Password that send via mail'}))
