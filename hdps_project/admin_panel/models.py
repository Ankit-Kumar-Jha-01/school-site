from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.class_name} "



class Student(models.Model):
    erp = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    admission_date = models.DateField()
    password = models.CharField(max_length=128)  # store hash, not plain text

    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.erp})"
    

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name
    

class Months(models.Model):
    month_name=models.CharField(max_length=20)

    def __str__(self):
        return self.month_name
    

class StudentFees(models.Model):
    STATUS_CHOICES = [('Paid', 'Paid'), ('Unpaid', 'Unpaid')]

    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.ForeignKey(Months, on_delete=models.CASCADE) 
    # month = models.CharField(max_length=20)
    # year = models.CharField(max_length=10)

    # Replacing fee1 to fee15 with meaningful fee components
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exam_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    library_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lab_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sports_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    computer_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smart_class_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    identity_card_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    annual_day_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transportation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    caution_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    misc_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        self.total = sum([
            self.tuition_fee, self.admission_fee, self.exam_fee, self.library_fee, self.lab_fee,
            self.sports_fee, self.computer_fee, self.development_fee, self.smart_class_fee, self.identity_card_fee,
            self.annual_day_fee, self.transportation_fee, self.caution_money, self.fine, self.misc_fee
        ])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - ₹{self.total}"




class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.uploaded_at.strftime('%Y-%m-%d')}"