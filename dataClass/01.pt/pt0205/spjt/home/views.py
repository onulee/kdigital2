from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'user_id':'aaa','nickName':'길동스'}
    # count='2day' -> 변수 count전송시킴
    return render(request,'index.html',context)
