from django.shortcuts import render

# Create your views here.
# main페이지
def index(request):
    return render(request,'index.html')