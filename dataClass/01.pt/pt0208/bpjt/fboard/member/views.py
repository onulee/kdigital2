from django.shortcuts import redirect, render, get_object_or_404
from member.models import Member

# 로그인 페이지
def login(request):
    return render(request,'login.html')

# 로그인 체크
def loginOk(request):
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    # id, pw가 일치하지 않을때 예외 처리
    try:
        member = Member.objects.get(m_id=id,m_pw=pw)
    except Member.DoesNotExist:
        member = None
    # member에 해당 id가 있으면
    if member:
        id = member.m_id
        name = member.m_name
        request.session['session_id']=id  # {'session_id':'aaa'}
        request.session['session_name']=name  # {'session_name':'name'}
        context ={'msg':'로그인 성공!!'}
        return render(request,'index.html',context)
    else:
        context ={'msg':'아이디와 패스워드가 일치하지 않습니다.'}
        return render(request,'login.html',context)
    
# 로그아웃
def logout(request):
    if request.session.get('session_id'):
        request.session.clear()              # 섹션모두 삭제
        # del request.session['session_id']  # 해당섹션만 삭제 
    return redirect('/')