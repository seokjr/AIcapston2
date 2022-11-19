from django.shortcuts import redirect, render

# Create your views here.
from .forms import *
from .models import *

next = 1
answers = 0

def level(request):    
    
    if request.method == 'POST':
        global next
        next += 1
        
        global answers
        answers = request.POST['answer']
        user = request.user
        answeraa = answer(
            answer=answers,
            user= user
        )
                                            
        answeraa.save()       
        
        d1 = TestImage.objects.get(test_id=next)        

       
       
        return render(request, 'level.html', {'n' : next,'title' : d1.title, 'img' : d1.imgfile})
    
    else:        
     
        next = 1
        
        d1 = TestImage.objects.get(test_id=next)        
        
     
        
        return render(request, 'level.html', {'n' : next,'title' : d1.title, 'img' : d1.imgfile})
