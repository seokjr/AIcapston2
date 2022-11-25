from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', board, name='board'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
    path('write/', fileUpload, name='write'),
    path('view/<int:pk>', boardview, name='view'),
    path('recommend/<int:user_id>',recommend, name='recommend'),

]


