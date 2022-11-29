from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *
from django.contrib import messages

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        img = request.POST['imgfile']
        content = request.POST['solimg']

        user = request.user
        board = Board(
            title=title,
            imgfile=img,
            content=content,
            user=user,
        )

        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board.html', context)

def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.solimg = request.POST['solimg']
        if request.FILES['imgfile'] is not None:
            board.imgfile = request.FILES['imgfile']
        board.user = request.user

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html', {'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def boardview(request,pk):
    board = Board.objects.get(id=pk)
    return render(request, 'view.html',{'view' : board})

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES['imgfile']
        content = request.FILES['solimg']
        user = request.user
        board = Board(
            title=title,
            solimg=content,
            imgfile=img,
            user=user,
        )
        board.save()
        return redirect('board')
    else:
        fileuploadForm = BoardForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'write.html', context)
    
def recommend(request, user_id):
    user = request.user.id
    if Grouprecommend.objects.filter(user_id = user):
        target = Grouprecommend.objects.filter(user_id = user).values('group_id')
        point = 0
        for key in target:
            if point == 0:
                uservalue1 = key['group_id']
            if point == 1:
                uservalue2 = key['group_id']
            if point == 2:
                uservalue3 = key['group_id']
            point += 1
        board = Board.objects.filter(user_id = uservalue1)
        board2 = Board.objects.filter(user_id = uservalue2)
        board3 = Board.objects.filter(user_id = uservalue3)
        if point == 1:
            board3 = ''
        elif point == 0:
            board2 = ''
            board3 = ''
        boardForm = BoardForm
        context = {
            'boardForm': boardForm,
            'board': board,
            'board2':board2,
            'board3':board3,
        }
        return render(request, 'recommend.html', context)
    else:
        messages.error(request,'추천이 안됐습니다! 초기 페이지로 갑니다.', extra_tags='danger')
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return redirect('board')
