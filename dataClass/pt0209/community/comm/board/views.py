from django.shortcuts import redirect, render
from board.models import Fboard
from django.db.models import Q
from django.core.paginator import Paginator

# 게시판리스트
def blist(request):
    # 현재페이지 받음, 없을때 1 고정
    nowpage = int(request.GET.get('nowpage',1))  
    
    if request.method == 'GET':
        # 모든 게시판 내용이 담겨있음.
        qs = Fboard.objects.all().order_by('-b_no')
        # 모든게시글을 받아서 페이지 분기 - 
        paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
        # 1,2,3 10개 blist에 담음
        blist = paginator.get_page(nowpage)
        context={'blist':blist,'nowpage':nowpage}
        return render(request,'blist.html',context) 
    else:
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        # title검색
        if category == 'title':
            qs = Fboard.objects.filter(b_title__contains=searchword)
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)
            context={'blist':blist,'nowpage':nowpage,'category':category,'searchword':searchword}
            return render(request,'blist.html',context)
            
        elif category == 'content':    
            qs = Fboard.objects.filter(b_content__contains=searchword)
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)
            context={'blist':blist,'nowpage':nowpage,'category':category,'searchword':searchword}
            return render(request,'blist.html',context)
        
        elif category == 'all':
            # a and b
            # qs = Fboard.objects.filter(b_title__contains=searchword,b_content__contains=searchword)
            # a or b
            qs = Fboard.objects.filter(Q(b_title__contains=searchword) | Q(b_content__contains=searchword))
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)       # paginator
            context={'blist':blist,'nowpage':nowpage,'category':category,'searchword':searchword}
            return render(request,'blist.html',context)
        

# 뷰페이지
def bview(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_hit += 1;
    qs.save()
    context={'board':qs}
    return render(request,'bview.html',context)

# 수정페이지
def bmodify(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context={'board':qs}
    return render(request,'bmodify.html',context)

# 수정페이지저장
def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    b_title = request.POST.get('b_title')
    b_content = request.POST.get('b_content')
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    qs.save()
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    # context = {"board":qs}
    return render(request,'bview.html',{"board":qs})
    # return redirect('board:bview')

# 게시판글쓰기
def bwrite(request):
    return render(request,'bwrite.html')

# 게시판글쓰기저장
def bwriteOk(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    qs = Fboard(b_id=id,b_title=title,b_content=content)
    qs.save()
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')

# 게시글 삭제
def bdelete(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('board:blist')