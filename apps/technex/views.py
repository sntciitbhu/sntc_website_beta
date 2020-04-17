from django.shortcuts import render
from django.http import HttpResponse

def technex(request):
    return HttpResponse('hello')