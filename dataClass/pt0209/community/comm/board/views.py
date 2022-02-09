from django.shortcuts import redirect, render
from board.models import Fboard

# 게시판리스트
def blist(request):
    if request.method == 'GET':
        qs = Fboard.objects.all().order_by('-b_no')
        context={'blist':qs}
        return render(request,'blist.html',context) 
    else:
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        # title검색
        if searchword == 'title':
            qs = Fboard.objects.filter(b_title__contains=searchword)
            context={'blist':qs}
            return render(request,'blist.html',context) 
            
        elif searchword == 'content':    
            qs = Fboard.objects.filter(b_content__contains=searchword)
            context={'blist':qs}
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