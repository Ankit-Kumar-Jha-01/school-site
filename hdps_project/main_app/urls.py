from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin-panel/', include('admin_panel.urls')),
    path('students/', include('students_app.urls')),
    path('gallery/', views.public_gallery, name='public_gallery'),
    path('about/', views.about_us, name='about_us'),
    path('admission_enquiry/', views.admission_enquiry, name='admission_enquiry'),
    path('contact_us/', views.contact_us, name='contact_us'),
]


