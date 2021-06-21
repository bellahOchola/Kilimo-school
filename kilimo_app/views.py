from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    all_class = ClassStreams.objects.all()

    if request.method == 'POST':
        form= ClassForm(request.POST, request.FILES)
        if form.is_valid():
            class_title = form.cleaned_data.get('class_title')
            form.save()

            return redirect('index')
    else:
        form = ClassForm()
    
    return render(request, 'index.html', {'form': form, 'all_class':all_class})


def single_class(request, id):
    one_class = ClassStreams.objects.get(id=id)

    return render(request, 'single_class.html', {'one_class':one_class})

def students(request):
    all_classes = ClassStreams.objects.all()
    all_students = Student.objects.all()

    if request.method == 'POST':
        form= StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            students_class = form.cleaned_data.get('student_class')
           
            form.save()

            return redirect('index')
    else:
        form = StudentsForm()

    return render(request, 'new_student.html', {'all_classes':all_classes, 'form':form, 'all_students':all_students})