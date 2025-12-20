from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_login, name='students_login'),  
    path('students/logout/', views.students_logout, name='students_logout'),
    path('students/profile/<str:erp>/', views.student_profile, name='student_profile'),
]
