from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def listorders(request):
    return HttpResponse('下面是系统中所有的订单信息。。。Yes!!!')

def listorders1(request):
    return HttpResponse('111')

def listorders2(request):
    return HttpResponse('222')

def listorders3(request):
    return HttpResponse('333')

def listorders4(request):
    return HttpResponse('444')