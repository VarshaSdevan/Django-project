from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Venue
from .models import Register

  
class VenueForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Venue
        # venue = models.ForeignKey('venue')
        fields = '__all__'

class RegisterForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Register
        # venue = models.ForeignKey('venue')
        fields = '__all__'