from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('task1/', views.task1, name='task1'),
    path('task2/', views.task2, name='task2'),
    path('calculate1/<int:task1_id>/', views.calculate1, name='calculate1'),
    path('calculate2/<int:task2_id>/', views.calculate2, name='calculate2'),
    path('delete1/<int:task1_id>/', views.delete1, name='delete1'),
    path('delete2/<int:task2_id>/', views.delete2, name='delete2'),

]