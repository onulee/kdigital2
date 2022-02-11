from django.shortcuts import redirect, render
from board.models import Fboard
from django.db.models import Q, F
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import Max,Min,Avg 
import urllib # 한글인코딩
import requests # 웹스크롤링
import json


#공공데이터
def publicData(request):
    m_serviceKey ='918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?serviceKey={}&pageNo=1&numOfRows=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'.format(m_serviceKey)
    response = requests.get(url)
    print("views response : ",response)
    # response의 내용을 text변환
    contents = response.text
    # text를 json 타입으로 변경
    json_ob = json.loads(contents)
    # json데이터 중 필요한 데이터 가져오기
    publicData = json_ob['response']['body']['items']['item']
    print(" views bodyData : ",publicData)
    context={'publicData':publicData}
    return render(request,'publicData.html',context)
    


# 게시판리스트
def blist(request):
    # 현재페이지 받음, 없을때 1 고정
    nowpage = int(request.GET.get('nowpage',1))  
    
    if request.method == 'GET':
        
        # 모든 게시판 내용이 담겨있음.
        qs = Fboard.objects.all().order_by('-b_group','b_step')
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
    # 파일이름 가져오기 
    b_img = request.FILES.get('b_img','')
    print("views file : ",request.FILES)
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    # 파일이름 저장
    qs.b_img = b_img
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
    member = Member.objects.get(m_id=id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img','')
    print("views file : ",request.FILES)
    
    # b_no 수동으로 1씩증가해서 저장시켜줌.
    no = Fboard.objects.aggregate(max_b_no=Max('b_no'))
    max_no = no['max_b_no']   # b_no 최대 번호를 찾음 1.2.5. ... 26
    max_no += 1          #최고 높은 숫자를 만들어줌. 27 = no+1
    b_no = max_no
    
    qs = Fboard(b_no=b_no,member=member,b_title=title,b_content=content,b_group=b_no,b_img=img)
    qs.save()
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')

# 게시글 삭제
def bdelete(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('board:blist')

# 답글쓰기
def breply(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context = {"board":qs}
    return render(request,'breply.html',context)


# 답글쓰기 저장
def breplyOk(request):
    # b_no 수동으로 1씩증가해서 저장시켜줌.
    no = Fboard.objects.aggregate(max_b_no=Max('b_no'))
    max_no = no['max_b_no']   # b_no 최대 번호를 찾음 1.2.5. ... 26
    max_no += 1          #최고 높은 숫자를 만들어줌. 27 = no+1
    b_no = max_no
    
    # 부모의 정보
    b_group = int(request.POST.get('b_group'))
    b_step = int(request.POST.get('b_step'))
    b_indent = int(request.POST.get('b_indent'))
    
    # 답글쓰기 내용
    id = request.POST.get('id')
    member = Member.objects.get(m_id=id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img','')
    
    # 부모의 b_group속한 게시글 b_step을 +1
    Fboard.objects.filter(b_group=b_group,b_step__gt=b_step).update(b_step=F('b_step')+1)
    
    # 부모의 bgroup,부모의 bstep+1, 부모의 b_indent+1
    qs = Fboard(b_no=b_no,member=member,b_title=title,b_content=content,b_group=b_group,b_step=b_step+1,b_indent=b_indent+1,b_img=img)
    qs.save()
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')
    
    