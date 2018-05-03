from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget =forms.PasswordInput)



class RegisterForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
                                attrs = {"class":"form-control",
                                          "placeholder":"Username"
                                  }),label='')
    email =forms.EmailField(widget = forms.TextInput(
                                attrs = {"class":"form-control",
                                          "placeholder":"Email"
                                            }),label='')
    password = forms.CharField(widget =forms.PasswordInput(attrs = {"class":"form-control",
                                                                    "placeholder":"Password"
                                                                            }),label='')
    password2 = forms.CharField(label ='' , widget = forms.PasswordInput(attrs = {"class":"form-control",
                                                                                                  "placeholder":"Confirm Password"
                                                                                                   }))
                                                                                               

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email =email)
        if qs.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs =User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Name is already taken")
        return username

    def clean(self):
        data =self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2!= password:
            raise forms.ValidationError("Password must match")
        return data
