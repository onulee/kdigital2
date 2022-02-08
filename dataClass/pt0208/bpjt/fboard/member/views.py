from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
    return render(request,'login.html')

def loginOk(request):
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    member = Member.objects.get(m_id=id,m_pw=pw)
    # member에 해당 id가 있으면
    if member:
        id = member.m_id
        name = member.m_name
        request.session['s_id']=id  # {'session_id':'aaa'}
    
    return render(request,'login.html')