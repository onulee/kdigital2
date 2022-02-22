from django.http import JsonResponse
from django.shortcuts import redirect, render
from board.models import Fboard
from board.models import Comment
from django.db.models import Q, F
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import Max,Min,Avg 
from django.core import serializers
from django.http import HttpResponse
import urllib # 한글인코딩
import requests # 웹스크롤링
import json
from django.forms.models import model_to_dict


# 공지사항 리스트
def notice(request):
    # 페이지 번호가 넘어와야 함.
    # page
    qs = Fboard.objects.all()
    context = {'blist':qs}
    return render(request,'customer/notice.html',context)

# 이벤트 뷰
def event_view(request,b_no):
    print("views b_no : ",b_no)
    context={"b_no":b_no}
    return render(request,'event/event_view.html',context)


# 하단댓글 리스트(Ajax) -게시글번호로 검색해서 가져옴.
def comlist(request):
    b_no = request.GET.get("b_no")
    print("views b_no : ",b_no)
    qs = Comment.objects.all().order_by('-c_no')
    clist = list(qs.values())
    return JsonResponse(clist,safe=False) # safe=False일때 list, safe=True일 때에는 dict타입이외, TypeError 예외 발생
    # clist = serializers.serialize('json', qs)
    # return HttpResponse(clist, content_type="text/json-comment-filtered")

# 하단댓글 삭제(Ajax)
def commdelete(request):
    c_no = request.GET.get('c_no')
    qs = Comment.objects.get(c_no=c_no)
    qs.delete()    
    context={'result':'댓글이 삭제되었습니다'}
    return JsonResponse(context)
 
# 댓글수정저장 
def commupdateok(request):
    c_no = request.GET.get('c_no')
    c_content = request.GET.get('c_content')
    qs = Comment.objects.get(c_no=c_no)
    qs.c_content = c_content
    qs.save()
    
    # qs = Comment.object.get(c_no=c_no)
    # qs = qs.__dict__
    # qs = del qs['_state']
    # return JsonResponse(qs, safe=False)
    
    context={
        "c_no": qs.c_no, 
        "member_id": qs.member_id, 
        "c_pw": qs.c_pw,
        "c_content":qs.c_content,
        "c_date":qs.c_date 
    }
    return JsonResponse(context)    

# 하단댓글 저장(Ajax)
def commwrite(request):
    # c_no 1씩증가 함수
    def comm_count():
        # c_no 수동으로 1씩증가해서 저장시켜줌.
        no = Comment.objects.aggregate(max_c_no=Max('c_no'))
        max_no = no['max_c_no']   # b_no 최대 번호를 찾음 1.2.5. ... 26
        max_no += 1          #최고 높은 숫자를 만들어줌. 27 = no+1
        return max_no
    # 1씩증가 함수 호출
    c_no = comm_count()
    
    id = request.session.get('session_id')  # session에서 id값 변수저장
    print("views id : ",id)
    # models 2.member객체
    member = Member.objects.get(m_id=id)
    b_no = request.GET.get("b_no")     # board b_no 변수저장
    # models 3.fboard객체
    fboard = Fboard.objects.get(b_no=b_no)
    # 4.c_pw
    c_pw = request.GET.get("c_pw")     #ajax으로 넘어온 pw 변수저장
    # 5.c_content
    c_content = request.GET.get("c_content")  #ajax으로 넘어온 content변수 저장
    # 6.c_date
    
    # 댓글저장
    qs = Comment(c_no=c_no,member=member,fboard=fboard,c_pw=c_pw,c_content=c_content)
    qs.save()
    context = {
        "c_no": qs.c_no, 
        "member_id": qs.member_id, 
        "c_pw": qs.c_pw,
        "c_content":qs.c_content,
        "c_date":qs.c_date }
    return JsonResponse(context)



#공공데이터
def publicData(request):
    nowpage = request.GET.get('nowpage',1)
    m_serviceKey ='918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?serviceKey={}&pageNo={}&numOfRows=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'.format(m_serviceKey,nowpage)
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

#공공데이터2
def publicData2(request):
    nowpage = request.GET.get('nowpage',1)
    m_serviceKey ='918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    url = 'https://api.odcloud.kr/api/apnmOrg/v1/list?page={}&perPage=20&serviceKey={}'.format(nowpage,m_serviceKey)
    # url에서 정보를 받아옴.
    response = requests.get(url)
    print("views response : ",response)
    # response의 내용을 text변환
    contents = response.text
    # text를 json 타입으로 변경
    json_ob = json.loads(contents)
    # json데이터 중 필요한 데이터 가져오기
    publicData = json_ob['data']
    print(" views bodyData : ",publicData)
    context={'publicData':publicData}
    return render(request,'publicData2.html',context)

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
    qs.b_hit += 1
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
    
    