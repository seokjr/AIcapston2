from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.POST['imgfile']
        user = request.user
        board = Board(
            title=title,
            content=content,
            imgfile=img,
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
        board.content = request.POST['content']
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
        content = request.POST['content']
        img = request.FILES['imgfile']
        user = request.user
        board = Board(
            title=title,
            content=content,
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
    
def boardrecommend(request, pk):
    user = request.user
    if Board.objects.filter(user_id = user) in Grouprecommend.objects.filter(group_id = user):
        board = Board.objects.get(id=pk)
    if request.method == 'POST':
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.imgfile = request.POST['imgfile']
        board.user = request.user

        return redirect('boardrecommend')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'boardrecommend.html', context)
