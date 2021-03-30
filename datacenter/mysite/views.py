from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    myName = "昇"
    return render(request,'index.html',locals())
