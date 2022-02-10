from django.shortcuts import render

# Create your views here.
def notice_list(request):
    return render(request,'notice_list.html')

def notice_read(request):
    return render(request,'notice_read.html')