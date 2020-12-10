from django import forms
from django.core.exceptions import ValidationError

class UserDataForm(forms.Form):
    positon = [
        ('Backend', 'Backend'),
        ('Mobile', 'Mobile')
    ]
    userName = forms.CharField(label='Applicant Name', max_length=256, required=True, \
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.EmailField(label='Email', max_length=256, required=True, \
        widget=forms.EmailInput(attrs={'placeholder': 'Applicant Email'}))

    phone = forms.CharField(label='Phone', max_length=14, required=True, \
        widget=forms.TextInput(attrs={'placeholder': 'Phone/Mobile Number: +88...'}))

    address = forms.CharField(label='Full Address', max_length=512, required=False, \
        widget=forms.TextInput(attrs={'placeholder': 'Full address'}))

    university = forms.CharField(label='Name Of University', max_length=256, required=True, \
        widget=forms.TextInput(attrs={'placeholder': 'University full name'}))

    graduationYear = forms.IntegerField(label='Graduation Year', min_value=2015, max_value=2020, required=True, \
        widget=forms.NumberInput(attrs={'placeholder': 'Graduation year between 2015 - 2020'}))
    
    cgpa = forms.DecimalField(label='CGPA', min_value=2.0, max_value=4.0, required=False, \
        widget=forms.NumberInput(attrs={'placeholder': 'CGPA between 2.0 - 4.0'}))

    experience = forms.IntegerField(label='Experience In Month', min_value=0, max_value=100, required=False, \
        widget=forms.NumberInput(attrs={'placeholder': 'Experience in month like 12'}))

    workPlace = forms.CharField(label='Current Work Place', max_length=256, required=False, \
        widget=forms.TextInput(attrs={'placeholder': 'Phone/Mobile Number: +88...'}))

    applyingIn = forms.ChoiceField(label='Applying In', choices=positon, required=True, \
        widget=forms.RadioSelect())

    salary = forms.IntegerField(label='Expected Salary', min_value=15000, max_value=60000, required=True, \
        widget=forms.NumberInput(attrs={'placeholder': 'Expected Salary like 35000'}))
    
    refference = forms.CharField(label='Field Buzz Refference', max_length=256, required=False, \
        widget=forms.TextInput(attrs={'placeholder': 'Name of refference, if no one write None'}))
    
    projectUrl = forms.URLField(label='Guthub Project URL', max_length=512, required=True, \
        widget=forms.URLInput(attrs={'placeholder': 'https://github.com/<user>/<repository>'}))
    
    cvFile = forms.FileField(label='Attach pdf format CV', widget=forms.FileInput(attrs={'accept':'application/pdf'}))

    def clean_cvFile(self):
        CV = self.cleaned_data.get('cvFile',True)
        if CV.size > (1024 * 1024 * 4):
            raise ValidationError("The maximum file size that can be uploaded is 4MB")
        else:
            return CV

    