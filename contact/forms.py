from django import forms
from .models import ContactForm
from django import forms

from django.forms import ModelForm
from django import forms
from .models import ContactForm1
# class FormContactForm(formsForm):
#     class Meta:
#         model= ContactForm
#         fields= ["fullname", "email", "contact", "message"]
from .models import User


class UserForm(ModelForm):

   # meta data for displaying a form
   class Meta:
      # model
      model = User

      # displaying fields
      fields = '__all__'

   # method for cleaning the data
   def clean(self):
      super(UserForm, self).clean()

      # getting username and password from cleaned_data
      username = self.cleaned_data['username']
      password = self.cleaned_data['password']

      # validating the username and password
      if len(username) < 5:
         self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

      if len(password) < 8:
         self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

      return self.cleaned_data


class FormContactForm(forms.ModelForm):
      class Meta:
        model = ContactForm1
        fields = ["fullname", "email", "contact", "message"]

        def __init__(self):
            self.cleaned_data = None

        def clean_fullname(self):
            valname=self.cleaned_data['fullname']
            if len(valname) < 5:
                raise forms.ValidationError('A minimum of 5 characters is required')
            return valname


        