from django.shortcuts import render

# Create your views here.
def regStudent(request):
    context ={'user_id':'aaa','user_pw':'1111'}
    stuStr = ['admin']
    return render(request,'reg.html',context)