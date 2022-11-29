from django.shortcuts import redirect, render

# Create your views here.
from .forms import *
from .models import *
from django.db.models import Count
from .ml import *

next = 1
answers = 0
totalnum = 0

def level(request):    
    
    if request.method == 'POST':
        global next
        next += 1
        
        global answers
        answers = request.POST['answer']
        user = request.user
        
        global totalnum
        
        #사용자 입력정보 불러오기
        d2 = TestImages.objects.get(test_id=next-1) 
        
        #사용자의 답이 맞는지 판단 
        if d2.answer == int(answers):
            a = 1
        else:
            a = 0
        
        #db저장
        answeraa = total(
            category=d2.title_id.title_id,
            correct = a,
            test_id_id=d2.test_id,
            user=user,
        )
                                            
        answeraa.save()       
        
        if next == 41:
            #유저가 푼 문제 중 카테고리 1번
            
            for i in range(1,9):    
                d3 = total.objects.filter(user_id = user) & total.objects.filter(category = i) & total.objects.filter(correct = 1)
                totalnum = d3.count()
                # tit = title.objects.get(title_id=i) 
                title_id = title.objects.get(title_id = i) 

                grades = grade( 
                    user=user,
                    total = totalnum,
                    title_id = title_id
                )
                
                grades.save()       
                
                gradetuple = grade.objects.filter(user_id = user)
            
            return render(request, 'result.html', {'gratetuple': gradetuple})
            
            
            
        #다음 이미지와 카테고리 불러오기
        d1 = TestImages.objects.get(test_id=next)        

       
       
        return render(request, 'level.html', {'n' : next,'title' : d1.title_id.title, 'img' : d1.imgfile})
    
    else:        
     
        next = 1
        d1 = TestImages.objects.get(test_id=next)        
        
     
        
        return render(request, 'level.html', {'n' : next,'title' : d1.title_id.title, 'img' : d1.imgfile})
