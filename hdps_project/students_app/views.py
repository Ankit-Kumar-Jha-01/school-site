from django.shortcuts import render
from django.http import HttpResponse
from admin_panel.models import Student, StudentFees
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


def students_login(request):
    if request.method == "POST":
        erp = request.POST.get("erp")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(erp=erp)
            if check_password(password, student.password):  # check hashed password
                fees = StudentFees.objects.filter(student=student)
                return render(request, "student_profile.html", {
                    "student": student,
                    "fees": fees
                })
            else:
                return render(request, "student_login.html", {"error": "Invalid ERP or Password"})
        except Student.DoesNotExist:
            return render(request, "student_login.html", {"error": "Invalid ERP or Password"})

    return render(request, "student_login.html")



def student_profile(request, erp):
    try:
        student = Student.objects.get(erp=erp)
        fees = StudentFees.objects.filter(student=student).select_related("month")
        return render(request, "student_profile.html", {
            "student": student,
            "fees": fees
        })
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)

# views.py
from django.shortcuts import redirect
from django.contrib.auth import logout

def students_logout(request):
    """
    Logs out the currently logged-in user and redirects to the login page.
    """
    logout(request)  # This clears the session and logs out the user
    return redirect('students_login')  # Replace 'login' with your login page URL name
