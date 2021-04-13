from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    MyName = "昇"
    data = [i for i in range(1,43)]
    random.shuffle(data)
    lotto_numbers = data[0:6]
    special_number = data[28]




    return render(request,'index.html',locals())
