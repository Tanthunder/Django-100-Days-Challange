from django.shortcuts import render , redirect
from .models import Student
from .forms import StudentForm
# Create your views here.

def read_all_data(request):
    """Retrieve all student objects and display them in template."""
    student_data = Student.objects.all()

    return render(request,'app1/index.html',{'student_data':student_data})

def read_specific_data(request,pk):
    """Retrieve specific student data and display in template."""
    student_data = Student.objects.get(id = pk)

    return render(request,'app1/specific-student-data.html',{'student_data':student_data})

def create_student(request):
    """insert student in db."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-data')
    form = StudentForm()
    return render(request,'app1/student_form.html',{'form':form})



def update_student(request,pk):
    """update existing student data."""
    stu = Student.objects.get(id=pk)
    form = StudentForm(instance=stu)
    if request.method == 'POST':
        #instance = stu is important, otherwise it will create new record.
        form = StudentForm(request.POST,instance = stu)
        if form.is_valid():
            form.save()
            return redirect('all-data')

    return render(request,'app1/student_form.html',{'form':form})

def delete_student(request,pk):
    """delete specific student."""
    Student.objects.get(id=pk).delete()
    return redirect('all-data')


