from django.shortcuts import render
from board.models import Board

# Create your views here.
def blist(request):
    qs = Board.objects.all().order_by('-b_group','b_step')
    context={'blist':qs}
    return render(request,'blist.html',context)
