from django.urls import path 
from . import views

urlpatterns=[
    path('sv/',views.Student_API.as_view()),
    path('sv/<int:pk>/',views.Student_API.as_view())
]