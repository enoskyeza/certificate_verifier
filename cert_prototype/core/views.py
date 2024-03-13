from django.shortcuts import render, get_object_or_404
from .models import Student
# Create your views here.
def student_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    print(f'Student Name: {student.name}')
    print(f'Course_status: {student.course_status}')
    print(f'Code url: {student.qr_code.url}')
    return render(request, 'student_details.html', {'student': student})
