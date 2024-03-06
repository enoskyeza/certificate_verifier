from django.urls import path
from .views import student_details

urlpatterns = [
    path("student/<int:student_id>/", student_details, name='student-details')
]