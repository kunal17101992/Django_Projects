from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpForm(forms.Form):

    Gchoice = [('Male','Male'),('Female','Female'),('Custom','Custom')]

    First_Name = forms.CharField()
    Surname = forms.CharField(required=False)
    Gender = forms.ChoiceField(choices=Gchoice, widget=forms.RadioSelect)
    Username = forms.CharField()
    Emailid = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Re_Enter_Password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data['Password']
        p2 = cleaned_data['Re_Enter_Password']

        if p1 != p2:
            raise forms.ValidationError("Password doesn't match")


    def clean_Username(self):
        count = User.objects.filter(username=self.cleaned_data['Username'].lower()).count()
        if count > 0:
            raise forms.ValidationError("Username already exist. Try another one!")
        return self.cleaned_data['Username']

    def clean_Emailid(self):
        count = User.objects.filter(email=self.cleaned_data['Emailid'].lower()).count()
        if count > 0:
            raise forms.ValidationError("Email id already exist. Click on Forgot username/password to know username and reset password")
        return self.cleaned_data['Emailid']

class SigninForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['Username'].strip().lower()
        password = cleaned_data['Password']

        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('Invalid Username/Password')
        else:
            if not user.is_active:
                print(user)
                raise forms.ValidationError('Account is not active. Did you verify your mail id?')
