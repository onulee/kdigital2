from django.shortcuts import render

# Create your views here.
def index(request):
    context={'user_id':'admin','u_count':100}
    return render(request,'index.html',context)