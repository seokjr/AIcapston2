from django.forms import ModelForm

from .models import *

class LevelForm(ModelForm):
    
    class Meta:
        model = TestImage
        fields = ['test_id','title','imgfile']