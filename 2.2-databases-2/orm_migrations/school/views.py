from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher, TeachersforStudent


def students_list(request):
    template = 'school/students_list.html'
    student_objects = Student.objects.all().order_by('group')
    teachers_for_student_objects = TeachersforStudent.objects.all()

    students ={'object_list':student_objects, 'teachers_for_student':teachers_for_student_objects}

    context = students
    
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)