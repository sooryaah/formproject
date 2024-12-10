from django.shortcuts import render,redirect,get_object_or_404
from foreignkeyapp.models import Course,Student
from .import views


# Create your views here.
def home(request):
    return render(request, 'home.html')
def course(request):
    return render(request,'add_course.html')
def student(request):
    return render(request,'add_student.html')
def show_student(request):
    return render(request,'show_details.html')


def add_coursedb(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')  
        course_fee = request.POST.get('fee')    
        
        course = Course(course_name=course_name, fee=course_fee)
        course.save()

        return redirect('add_student')
    
    return render(request, 'add_course.html')

def add_student(request):
    courses=Course.objects.all()
    return render(request,'add_student.html',{'course':courses})
def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        student_address=request.POST['student_address']
        age=request.POST['age']
        jdate=request.POST['date']
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('show_details')


def show_details(request):
    students = Student.objects.all()  # Fetch all students from the database
    return render(request, 'show_details.html', {'students': students})  # Pass the 'students' context to the template


def delete_student(request,student_id):
    emp=Student.objects.get(id=student_id)
    emp.delete()
    return redirect('show_details')

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()
    
    if request.method == "POST":
        # Get data from the form
        student.student_name = request.POST.get('student_name')
        student.student_address = request.POST.get('student_address')
        student.student_age = request.POST.get('student_age')
        student.joining_date = request.POST.get('joining_date')
        course_id = request.POST.get('course')
        student.course = get_object_or_404(Course, id=course_id)
        student.save()  # Save changes to the database
        return redirect('show_details')  # Redirect to the student details page
    
    return render(request, 'edit_student.html', {
        'student': student,
        'courses': courses,
    })

