from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

next = 1

def level(request):    
    
    if request.method == 'POST':
        global next
        next = next + 1
        # form = LevelForm(request.POST)
        # form.save()
       
       
        return render(request, 'level.html', {'n' : next})
    
    else:        
     
        next = 1
       
        # form = LevelForm()
        
        
        return render(request, 'level.html', {'n' : next},)
