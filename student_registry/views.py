from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def student_list(request):  
    students=Student.objects.all()
    return render(request,'C:/Users/prave/OneDrive/Desktop/Day 1/students/student_registry/templates/student_list.html',{'students':students})
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')
        Student.objects.create(name=name, course=course, email=email)
        return redirect('student_list')
    return render(request,'add_student.html')