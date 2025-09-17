from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_admin, name='login'),
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('student/', views.student, name='student_dashboard'),
    path('new-student/', views.register_student, name='register_student'),
    path('update-student/', views.update_student, name='update_student'),
    path('fees-update',views.fees_entry, name='fees_entry'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/delete/<int:image_id>/', views.delete_image, name='delete_image'),

]