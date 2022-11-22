from django.shortcuts import redirect, render

# Create your views here.
from .models import *

from test.models import *

# Create your views here.

def testresult(request):
    user = request.user
    gradetuple = grade.objects.filter(user_id = user)
    
    return render(request, 'testresult.html', {'gratetuple': gradetuple})
