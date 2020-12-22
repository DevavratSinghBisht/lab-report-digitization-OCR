from django import forms
from .models import *

class UpdateForm(forms.ModelForm):


    class Meta:
        model = Thyrocare
        fields = '__all__'