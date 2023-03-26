from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    students = Student.objects.prefetch_related('teachers').order_by(ordering)
    template = 'school/students_list.html'
    object_list = {'students': students}
    return render(request, template, object_list)
