from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(label ='',widget = forms.TextInput(
                                attrs = {"class":"form-control",
                                "placeholder":"Fullname" ,
                                  }))
    email = forms.EmailField(label ='',widget = forms.EmailInput(
                                         attrs = {"class":"form-control",
                                         "placeholder":"Email"
                                         }))
    content = forms.CharField(label ='',widget = forms.Textarea(
                                         attrs = {"class":"form-control",
                                         "placeholder":"Message"
                                          }))

    def clean_email(self):
        email =cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email
