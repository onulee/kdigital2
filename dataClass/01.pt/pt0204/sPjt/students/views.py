from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student
from django.shortcuts import render

# 학생등록페이지
def regStudent(request):
    print("view student>reg호출")
    return render(request,'reg.html')

# 학생등록 db 저장
def regStuCon(request):
    name = request.POST['name']
    print("students view : ",name)
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
    print("views qs : ",qs)
    qs.save()
    
    # students:stuAll
    return HttpResponseRedirect(reverse('students:reg'))