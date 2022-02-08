from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from board.models import Freeboard

# 게시판리스트
def blist(request):
    qs = Freeboard.objects.all().order_by('-b_no')
    context = {'blist':qs }
    return render(request,'blist.html',context)

# 게시판 글쓰기
def bwrite(request):
    return render(request,'write_view.html')

# 게시판글쓰기 저장
def bwriteOk(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    qs = Freeboard(b_id=id,b_title=title,b_content=content)
    qs.save()
    
    return HttpResponseRedirect(reverse('board:blist'))

def bview(request,b_no):
    
    context={}
    return render(request,'content_view.html',context)