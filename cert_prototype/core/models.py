from django.db import models

# Create your models here.
# core/models.py

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    pay_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')])
    course_status = models.CharField(max_length=20, choices=[('complete', 'Complete'), ('enrolling', 'Enrolling')])
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_of_issuance = models.DateField()