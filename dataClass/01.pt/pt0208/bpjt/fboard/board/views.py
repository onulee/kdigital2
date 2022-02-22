import datetime
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

# 게시판 뷰페이지
def bview(request,b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    qs.b_hit = qs.b_hit+1
    qs.save()
    context={'board':qs}
    return render(request,'content_view.html',context)

# 게시판 수정페이지
def bmodify(request,b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    context={'board':qs}
    return render(request,'modify_view.html',context)

# 게시판수정 저장
def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    title = request.POST.get('title')
    content = request.POST.get('content')
    qs = Freeboard.objects.get(b_no=b_no)
    qs.b_title = title
    qs.b_content = content
    qs.b_date = datetime.datetime.now()   #2개 1개 최초등록, 수정업데이트
    # qs.b_date = timezone.now()    #2개 1개 최초등록, 수정업데이트
    qs.save()
    
    return HttpResponseRedirect(reverse('board:blist'))

# 게시판 삭제
def bdelete(request,b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    qs.delete()
    return HttpResponseRedirect(reverse('board:blist'))