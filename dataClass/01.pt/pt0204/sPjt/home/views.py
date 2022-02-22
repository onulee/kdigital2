from django.shortcuts import render

# Create your views here.
def index(request):
    print("home>index호출")
    return render(request,'index.html')