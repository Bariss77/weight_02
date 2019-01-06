from django import forms
from my_app.models import *

class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        fields = ('weight',)
