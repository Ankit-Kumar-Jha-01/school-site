from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render
from admin_panel.models import GalleryImage

def home(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')[:6]  # latest 6 images
    return render(request, 'home.html', {'images': images})

def public_gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'public_gallery.html', {'images': images})

def about_us(request):
    return render(request, 'about_us.html')


def admission_enquiry(request):
    return render(request, 'admission_enquiry.html')

def contact_us(request):
    return render(request, 'contact_us.html')