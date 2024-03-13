from django.db import models
from django.urls import reverse
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings


# Create your models here.
# core/models.py

class Student(models.Model):
    COURSE_CHOICES = [
        ('FLD', 'Fresh Learner Driving'),
        ('ALD', 'Advanced Learner Driving'),
        ('DD', 'Defensive Driving')
    ]

    COURSE_STATUS = [
        ('complete', 'Complete'),
        ('enrolling', 'Enrolling'),
    ]

    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, null=True, blank=True)
    student_id = models.CharField(max_length=10, unique=True)  # Self generating
    # pay_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')])
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    issue_date = models.DateField(null=True, blank=True)
    course_status = models.CharField(max_length=20, choices=COURSE_STATUS)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate a URL  for the student detail view
        super().save(*args, **kwargs)
        student_detail_url = f"{settings.BASE_URL}{reverse('student-details', args=[self.pk])}"

        # Generate QR code content with the student detail URL
        # qr_content = f"Student Detail URL: {student_detail_url}\nName: {self.name}\nCourse Status: {self.get_course_status_display()}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(student_detail_url)
        qr.make(fit=True)

        # Save the generated QR code as an image file
        buffer = BytesIO()
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(buffer)

        # Set the QR code image to the student instance
        self.qr_code.save(f'qr_code_{self.pk}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    # PREVIOUS QR GENERATOR
    # def save(self, *args, **kwargs):
    #     # Generate and save QR code
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     qr.add_data(f"Student ID: {self.id}\nName: {self.name}\nCourse Status: {self.course_status}")
    #     qr.make(fit=True)
    #
    #     img = qr.make_image(fill_color="black", back_color="white")
    #
    #     # Save the generated QR code as an image file
    #     buffer = BytesIO()
    #     img.save(buffer)
    #     self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
    #
    #     super().save(*args, **kwargs)


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_of_issuance = models.DateField()
