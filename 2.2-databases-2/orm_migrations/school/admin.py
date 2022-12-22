from django.contrib import admin
from .models import Student, Teacher, TeachersforStudent


class TeachersforStudentInLine(admin.TabularInline):
    model = TeachersforStudent
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [TeachersforStudentInLine]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    
