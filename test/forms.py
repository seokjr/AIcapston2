from django.forms import ModelForm

from .models import *

class LevelForm(ModelForm):
    class Meta:
        model = LevelTests
        fields = ['answer']