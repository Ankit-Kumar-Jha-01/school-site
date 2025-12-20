from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Class, Student, Subject, StudentFees, Months, GalleryImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html')

# @login_required
def login_admin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {"error":"user is not verified"})
        
    else:
        return render (request, 'admin_login.html')

def dashboard(request):
    return render(request, 'admin_dashboard.html')

def student(request):
    return render(request, 'student_dashboard.html')

def register_student(request):
    classes=Class.objects.all()
    if request.method=='POST':
        
        selected_class=Class.objects.get(class_id=request.POST.get('class_id'))
        
        new_students=Student(
            erp=request.POST.get('erp'),
            first_name=request.POST.get('first_name'),
            middle_name=request.POST.get('middle_name'),
            last_name=request.POST.get('last_name'),
            gender =request.POST.get('gender'),
            dob = request.POST.get('dob'),
            class_id =selected_class,
            address = request.POST.get('address'),
            contact_number =request.POST.get('contact_number'),
            email = request.POST.get('email'),
            admission_date =request.POST.get('admission_date'),
            password=make_password(request.POST.get('password'))
        )
        new_students.save()
       
        return render(request, 'register_student.html', {
            "success":"you have successfully registered with ERP",
            "new_students":new_students.erp,
            'classes': classes  
        })

    return render(request, 'register_student.html', {'classes': classes})

def fees_entry(request):
    student = None
    months = Months.objects.all()

    if request.method == 'POST':
        erp = request.POST.get('erp')

        try:
            student = Student.objects.get(erp=erp)
        except Student.DoesNotExist:
            return render(request, 'fees.html', {'error': 'No student with this ERP'})

        if 'submit_fees' in request.POST:
            for month in months:
                tuition_fee = float(request.POST.get(f'tuition_fee_{month.id}') or 0)
                admission_fee = float(request.POST.get(f'admission_fee_{month.id}') or 0)
                exam_fee = float(request.POST.get(f'exam_fee_{month.id}') or 0)
                library_fee = float(request.POST.get(f'library_fee_{month.id}') or 0)
                lab_fee = float(request.POST.get(f'lab_fee_{month.id}') or 0)
                sports_fee = float(request.POST.get(f'sports_fee_{month.id}') or 0)
                computer_fee = float(request.POST.get(f'computer_fee_{month.id}') or 0)
                development_fee = float(request.POST.get(f'development_fee_{month.id}') or 0)
                smart_class_fee = float(request.POST.get(f'smart_class_fee_{month.id}') or 0)
                identity_card_fee = float(request.POST.get(f'identity_card_fee_{month.id}') or 0)
                annual_day_fee = float(request.POST.get(f'annual_day_fee_{month.id}') or 0)
                transportation_fee = float(request.POST.get(f'transportation_fee_{month.id}') or 0)
                caution_money = float(request.POST.get(f'caution_money_{month.id}') or 0)
                fine = float(request.POST.get(f'fine_{month.id}') or 0)
                misc_fee = float(request.POST.get(f'misc_fee_{month.id}') or 0)

                StudentFees.objects.create(
                    student=student,
                    month=month,   
                    tuition_fee=tuition_fee,
                    admission_fee=admission_fee,
                    exam_fee=exam_fee,
                    library_fee=library_fee,
                    lab_fee=lab_fee,
                    sports_fee=sports_fee,
                    computer_fee=computer_fee,
                    development_fee=development_fee,
                    smart_class_fee=smart_class_fee,
                    identity_card_fee=identity_card_fee,
                    annual_day_fee=annual_day_fee,
                    transportation_fee=transportation_fee,
                    caution_money=caution_money,
                    fine=fine,
                    misc_fee=misc_fee,
                    status="Unpaid"
                )

            return render(request, 'fees.html', {
                'success': 'Fees successfully recorded!',
                
                'months': months
            })

    return render(request, 'fees.html', {'months': months})

def update_student(request):
    return render(request, 'update_student.html')



def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')

    
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        GalleryImage.objects.create(image=uploaded_file)
        return redirect('gallery')

    return render(request, 'gallery.html', {
        'images': images
    })

def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    image.delete()
    return redirect('gallery')

