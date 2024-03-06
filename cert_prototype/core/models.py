from django.db import models

# Create your models here.
# core/models.py

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    pay_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')])
    course_status = models.CharField(max_length=20, choices=[('complete', 'Complete'), ('enrolling', 'Enrolling')])
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate and save QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"Student ID: {self.id}\nName: {self.name}\nCourse Status: {self.course_status}")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the generated QR code as an image file
        buffer = BytesIO()
        img.save(buffer)
        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_of_issuance = models.DateField()