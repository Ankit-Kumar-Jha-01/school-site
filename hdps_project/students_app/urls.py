from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.students_login, name='students_login'),
    path("student-profile/<str:erp>/", views.student_profile, name="student_profile"),
    path('logout/', views.students_logout, name='logout'),
]